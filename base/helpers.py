from django.conf import settings
from django.core.cache import cache
from dateutil.parser import parse
from requests import post
from bs4 import BeautifulSoup


def _raw_api_request(username, password, action, extra_params=""):
    headers = {
        "SOAPAction": "http://edupoint.com/webservices/ProcessWebServiceRequest",
        "Content-Type": "text/xml"
    }
    xml = """
        <v:Envelope xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns:d="http://www.w3.org/2001/XMLSchema" xmlns:c="http://schemas.xmlsoap.org/soap/encoding/"
        xmlns:v="http://schemas.xmlsoap.org/soap/envelope/">
          <v:Header />
          <v:Body>
            <ProcessWebServiceRequest xmlns="http://edupoint.com/webservices/" id="o0" c:root="1">
              <userID i:type="d:string">{}</userID>
              <password i:type="d:string">{}</password>
              <skipLoginLog i:type="d:string">false</skipLoginLog>
              <parent i:type="d:string">false</parent>
              <webServiceHandleName i:type="d:string">PXPWebServices</webServiceHandleName>
              <methodName i:type="d:string">{}</methodName>
              <paramStr i:type="d:string">&lt;Parms&gt;&lt;ChildIntID&gt;0&lt;/ChildIntID&gt;{}&lt;/Parms&gt;</paramStr>
            </ProcessWebServiceRequest>
          </v:Body>
        </v:Envelope>
        """
    print(xml.format(username, password, action, extra_params))
    r = post(settings.SIS_ENDPOINT, data=xml.format(username, password, action, extra_params), headers=headers)
    return r.text.replace("&lt;", "<").replace("&gt;", ">")


def api_request(username, password, action, extra_params=""):
    content = _raw_api_request(username, password, action, extra_params)
    parsed = BeautifulSoup(content, "xml")
    return parsed


def check_auth(request):
    xml_data = base_data(request, "GetPXPMessages")
    if xml_data.find("RT_ERROR"):
        return {"error": "Invalid Username/Password."}


def base_data(request, action, extra_params=""):
    xml_data = api_request(username=request.POST.get("username"),
                           password=request.POST.get("password"),
                           action=action,
                           extra_params=extra_params)
    return xml_data


def get_user_data(request):
    key = "{}:{}".format(request.POST.get("username"), "ChildList")
    bad_auth = check_auth(request)
    if not bad_auth:
        cached = cache.get(key)
        if cached and not request.POST.get("force"):
            return cached
        xml_data = base_data(request, "ChildList")
        data = dict()
        data['username'] = request.POST.get("username")
        ch = xml_data.find("Child")
        data['full_name'] = ch.find("ChildName").get_text()
        data['school_name'] = ch.find("OrganizationName").get_text()
        data['grade'] = ch.find("Grade").get_text()
        data['photo'] = ch.find("photo").get_text()
        data.update(get_schedule(request))
        cache.set(key, data, 600)
        return data
    else:
        if cache.get(key):
            cache.delete(key)
        return bad_auth


def get_schedule(request):
    key = "{}:{}".format(request.POST.get("username"), "StudentClassList")
    bad_auth = check_auth(request)
    if not bad_auth:
        cached = cache.get(key)
        if cached and not request.POST.get("force"):
            return cached
        xml_data = base_data(request, "StudentClassList")
        data = dict()
        classes = []
        for c in xml_data.find_all("ClassListing"):
            class_data = dict()
            class_data['period'] = c.get("Period")
            class_data['name'] = c.get("CourseTitle")
            class_data['location'] = c.get("RoomName")
            class_data['teacher'] = c.get("Teacher")
            classes.append(class_data)
        data['schedule'] = list(sorted(classes, key=lambda c: int(c['period'])))
        cache.set(key, data, 600)
        return data
    else:
        if cache.get(key):
            cache.delete(key)
        return bad_auth


def get_quarter_grades(request, q):
    key = "{}:{}".format(request.POST.get("username"), "Quarter{}".format(q.get("Index")))
    bad_auth = check_auth(request)
    if not bad_auth:
        cached = cache.get(key)
        if cached and not request.POST.get("force"):
            return cached
        xml_data = base_data(request, "Gradebook",
                             extra_params="&lt;ReportPeriod&gt;{}&lt;/ReportPeriod&gt;".format(q.get("Index")))
        data = dict()
        classes = []
        for c in xml_data.find_all("Course"):
            class_data = dict()
            class_data['period'] = c.get("Period")
            class_data['name'] = c.get("Title")
            class_data['location'] = c.get("Room")
            class_data['teacher'] = c.get("Staff")
            m = c.find("Mark")
            class_data['grade_letter'] = m.get("CalculatedScoreString")
            class_data['grade_percentage'] = m.get("CalculatedScoreRaw")
            assignments = []
            for a in c.find_all("Assignment"):
                assignment_data = dict()
                assignment_data['name'] = a.get("Measure")
                assignment_data['assignment_type'] = a.get("Type")
                assignment_data['date'] = parse(a.get("Date")).date()
                assignment_data['due_date'] = parse(a.get("DueDate")).date()
                assignment_data['score'] = a.get("Score")
                assignment_data['points'] = a.get("Points")
                assignment_data['notes'] = a.get("Notes")
                assignments.append(assignment_data)
            class_data['assignments'] = assignments
            classes.append(class_data)
        data['courses'] = list(sorted(classes, key=lambda c: int(c['period'])))
        data['start_date'] = parse(q.get("StartDate")).date()
        data['end_date'] = parse(q.get("EndDate")).date()
        data['name'] = q.get("GradePeriod")
        cache.set(key, data, 600)
        return data
    else:
        if cache.get(key):
            cache.delete(key)
        return bad_auth


def get_year_data(request):
    key = "{}:{}".format(request.POST.get("username"), "Year")
    bad_auth = check_auth(request)
    if not bad_auth:
        cached = cache.get(key)
        if cached and not request.POST.get("force"):
            return cached
        xml_data = base_data(request, "Gradebook")
        data = dict()
        quarters = []
        for q in xml_data.find_all("ReportPeriod"):
            quarters.append(get_quarter_grades(request, q))
        data['quarters'] = quarters
        cache.set(key, data, 600)
        return data
    else:
        if cache.get(key):
            cache.delete(key)
        return bad_auth
