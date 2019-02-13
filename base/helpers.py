from django.conf import settings
from django.core.cache import cache
from django.utils import timezone
from dateutil.parser import parse
from html import unescape
from requests import post
from bs4 import BeautifulSoup
from xml.sax.saxutils import escape


def _raw_api_request(username, password, action, extra_params=""):
    headers = {
        "User-Agent": "kSOAP/2.0",
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
              <skipLoginLog i:type="d:string">true</skipLoginLog>
              <parent i:type="d:string">false</parent>
              <webServiceHandleName i:type="d:string">PXPWebServices</webServiceHandleName>
              <methodName i:type="d:string">{}</methodName>
              <paramStr i:type="d:string">&lt;Parms&gt;&lt;ChildIntID&gt;0&lt;/ChildIntID&gt;{}&lt;/Parms&gt;</paramStr>
            </ProcessWebServiceRequest>
          </v:Body>
        </v:Envelope>
        """
    r = post(settings.SIS_ENDPOINT, data=xml.format(username, escape(password), action, extra_params), headers=headers) # , verify=False)
    return unescape(r.text)


def api_request(username, password, action, extra_params=""):
    content = _raw_api_request(username, password, action, extra_params)
    parsed = BeautifulSoup(str(content), "xml")
    return parsed


def base_data(request, action, extra_params=""):
    saved_password = ""
    if request.user.encrypted_password:
        saved_password = settings.CIPHER.decrypt(request.user.encrypted_password)
    xml_data = api_request(username=request.user.username,
                           password=request.session.get("password", saved_password),
                           action=action,
                           extra_params=extra_params)
    return xml_data


def get_user_data(request):
    key = "{}:{}".format(request.user.username, "ChildList")
    cached = cache.get(key)
    if cached and not request.GET.get("force"):
        return cached
    xml_data = base_data(request, "ChildList")
    data = dict()
    data['username'] = request.user.username
    ch = xml_data.find("Child")
    data['full_name'] = ch.find("ChildName").get_text()
    data['school_name'] = ch.find("OrganizationName").get_text()
    data['grade'] = ch.find("Grade").get_text()
    data['photo'] = ch.find("photo").get_text()
    data.update(get_schedule(request))
    cache.set(key, data, 60 * 60 * 24 * 7)
    return data


def get_schedule(request):
    key = "{}:{}".format(request.user.username, "StudentClassList")
    cached = cache.get(key)
    if cached and not request.GET.get("force"):
        return cached
    xml_data = base_data(request, "StudentClassList")
    data = dict()
    classes = []
    for c in xml_data.find_all("ClassListing"):
        class_data = dict()
        class_data['period'] = c.get("Period") if c.get("Period").isdigit() else c.get("Period")[0]
        class_data['name'] = c.get("CourseTitle")
        class_data['location'] = c.get("RoomName")
        class_data['teacher'] = c.get("Teacher")
        classes.append(class_data)
    data['schedule'] = list(sorted(classes, key=lambda c: int(c['period'])))
    cache.set(key, data, 60 * 30)
    return data


def get_quarter_grades(request, qnum, periodnum, skip_courses=False, skip_assignments=False):
    if qnum and skip_courses:
        part2 = "Quarter{}:NoGrades".format(qnum)
    elif qnum and skip_assignments:
        part2 = "Quarter{}:NoAssignments".format(qnum)
    elif qnum:
        part2 = "Quarter{}".format(qnum)
    elif periodnum:
        part2 = "Period{}".format(periodnum)
    else:
        part2 = "Current"
    key = "{}:{}".format(request.user.username, part2)
    cached = cache.get(key)
    if cached and not request.GET.get("force"):
        return cached
    xml_data = base_data(request, "Gradebook",
                         extra_params="&lt;ReportPeriod&gt;{}&lt;/ReportPeriod&gt;".format(qnum) if qnum else "")
    data = dict()
    if not skip_courses:
        classes = []
        for c in xml_data.find_all(lambda l: l.name == "Course" and (l.get("Period") == periodnum if periodnum else True)):
            class_data = dict()
            class_data['period'] = c.get("Period") if c.get("Period").isdigit() else c.get("Period")[0]
            class_data['name'] = c.get("Title")
            class_data['location'] = c.get("Room")
            class_data['teacher'] = c.get("Staff")
            grades = dict()
            for m in c.find_all("Mark"):
                name = m.get("MarkName")
                grade_data = dict()
                grade_data['letter'] = m.get("CalculatedScoreString")
                grade_data['percentage'] = m.get("CalculatedScoreRaw")
                breakdown = dict()
                for summary in m.find_all("GradeCalculationSummary"):
                    for gc in summary.find_all("AssignmentGradeCalc"):
                        breakdown[gc.get("Type")] = {
                            'points': gc.get("Points"),
                            'points_possible': gc.get("PointsPossible"),
                            'weight': gc.get("Weight").strip("%"),
                            'letter_grade': gc.get("CalculatedMark"),
                            'percentage': gc.get("WeightedPct").strip("%")
                        }
                grade_data['breakdown'] = breakdown
                if name == "1st Qtr":
                    grades['first_quarter'] = grade_data
                elif name == "2nd Qtr":
                    grades['second_quarter'] = grade_data
                elif name == "3rd Qtr":
                    grades['third_quarter'] = grade_data
                elif name == "4th Qtr":
                    grades['fourth_quarter'] = grade_data
                elif name == "1st Semester":
                    grades['first_semester'] = grade_data
                elif name == "2nd Semester":
                    grades['second_semester'] = grade_data
            class_data['grades'] = grades
            if not skip_assignments:
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
    q = xml_data.find(lambda l: l.name == "ReportPeriod" and (l.get("Index") == qnum if qnum else parse(
        l.get("StartDate")).date() <= timezone.now().date() <= parse(l.get("EndDate")).date()))
    if not q:
        return {'error': 'No quarter found with index {}.'.format(qnum)}
    data['index'] = q.get("Index")
    data['start_date'] = parse(q.get("StartDate")).date()
    data['end_date'] = parse(q.get("EndDate")).date()
    data['name'] = q.get("GradePeriod")
    cache.set(key, data, 60 * 30)
    return data


def get_report_card(request):
    key = "{}:{}".format(request.user.username, "ReportCard")
    cached = cache.get(key)
    if cached and not request.GET.get("force"):
        return cached
    xml_data = base_data(request, "Gradebook")
    data = dict()
    courses = dict()
    for q in xml_data.find_all("ReportPeriod"):
        qdata = get_quarter_grades(request, qnum=q.get("Index"), periodnum="", skip_assignments=True)
        for course in qdata['courses']:
            if course['period'] not in courses:
                courses[course['period']] = course
            courses[course['period']]['grades'].update(course['grades'])
    data['courses'] = [courses[k] for k in sorted(courses)]
    cache.set(key, data, 60 * 60 * 24 * 7)
    return data


def get_year_data(request):
    key = "Year"
    cached = cache.get(key)
    if cached and not request.GET.get("force"):
        return cached
    xml_data = base_data(request, "Gradebook")
    data = dict()
    quarters = []
    for q in xml_data.find_all("ReportPeriod"):
        qdata = get_quarter_grades(request, qnum=q.get("Index"), periodnum="", skip_courses=True)
        quarters.append(qdata)
    data['quarters'] = quarters
    cache.set(key, data, 60 * 60 * 24 * 7 * 4)
    return data
