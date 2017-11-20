from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuarterSerializer, UserSerializer, YearSerializer
from .helpers import get_quarter_grades, get_user_data, get_year_data


class GradeView(APIView):
    def post(self, request, format=None, **kwargs):
        raw_data = get_quarter_grades(request, str(self.kwargs.get('qnum', "")), str(self.kwargs.get('period', "")))
        if raw_data.get("error"):
            return Response(raw_data)
        serializer = QuarterSerializer(raw_data)
        return Response(serializer.data)


class RootView(APIView):
    def get(self, request, format=None):
        data = {
            "info": "All requests must be POST requests with username and password in the POST data.",
            "/user/": "User information",
            "/quarters/": "List of quarters",
            "/grades/": "Current grades",
            "/grades/quarter/<id>/": "Grades for given quarter",
            "/grades/class/<period>/": "Grades for a given period for the current quarter",
        }
        return Response(data)


class UserView(APIView):
    def post(self, request, format=None):
        raw_data = get_user_data(request)
        if raw_data.get("error"):
            return Response(raw_data)
        serializer = UserSerializer(raw_data)
        return Response(serializer.data)


class YearView(APIView):
    def post(self, request, format=None):
        raw_data = get_year_data(request)
        if raw_data.get("error"):
            return Response(raw_data)
        serializer = YearSerializer(raw_data)
        return Response(serializer.data)
