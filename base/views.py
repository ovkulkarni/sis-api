from collections import OrderedDict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import QuarterSerializer, UserSerializer, YearSerializer
from .helpers import get_quarter_grades, get_user_data, get_year_data


class GradeView(APIView):
    def get(self, request, format=None, **kwargs):
        raw_data = get_quarter_grades(request, str(self.kwargs.get('qnum', "")), str(self.kwargs.get('period', "")))
        if raw_data.get("error"):
            return Response(raw_data)
        serializer = QuarterSerializer(raw_data)
        return Response(serializer.data)


class RootView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        data = OrderedDict({
            "info": "All requests must be GET requests using HTTP Basic Auth.",
            request.build_absolute_uri("/user/"): "User information",
            request.build_absolute_uri("/quarters/"): "List of quarters",
            request.build_absolute_uri("/grades/"): "Current grades",
            "/grades/quarter/<id>/": "Grades for given quarter",
            "/grades/class/<period>/": "Grades for a given period for the current quarter",
        })
        return Response(data)


class UserView(APIView):
    def get(self, request, format=None):
        raw_data = get_user_data(request)
        if raw_data.get("error"):
            return Response(raw_data)
        serializer = UserSerializer(raw_data)
        return Response(serializer.data)


class YearView(APIView):
    def get(self, request, format=None):
        raw_data = get_year_data(request)
        if raw_data.get("error"):
            return Response(raw_data)
        serializer = YearSerializer(raw_data)
        return Response(serializer.data)


def logout(request):
    request.session.clear()
    return redirect("//log:out@{}/".format(request.get_host()))
