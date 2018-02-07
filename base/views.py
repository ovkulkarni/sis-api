from collections import OrderedDict
from django.shortcuts import redirect
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import QuarterSerializer, ReportCardSerializer, UserSerializer, YearSerializer
from .helpers import get_quarter_grades, get_report_card, get_user_data, get_year_data


class GradeView(APIView):
    def get(self, request, format=None, **kwargs):
        if request.user and request.user.username == settings.TEST_USER:
            return Response(settings.TEST_GRADE_DATA)
        raw_data = get_quarter_grades(request, str(self.kwargs.get('qnum', "")), str(self.kwargs.get('period', "")))
        serializer = QuarterSerializer(raw_data)
        return Response(serializer.data)


class ReportCardView(APIView):
    def get(self, request, format=None):
        if request.user and request.user.username == settings.TEST_USER:
            return Response(settings.TEST_REPORT_CARD_DATA)
        raw_data = get_report_card(request)
        serializer = ReportCardSerializer(raw_data)
        return Response(serializer.data)


class RootView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        data = OrderedDict((
            ("info", "All requests must be GET requests using HTTP Basic Auth."),
            (request.build_absolute_uri("/user/"), "User information"),
            (request.build_absolute_uri("/quarters/"), "List of quarters"),
            (request.build_absolute_uri("/grades/"), "Current grades"),
            (request.build_absolute_uri("/report_card/"), "Report card"),
            ("/grades/quarter/<id>/", "Grades for given quarter"),
            ("/grades/class/<period>/", "Grades for a given period for the current quarter"),
        ))
        return Response(data)


class UserView(APIView):
    def get(self, request, format=None):
        if request.user and request.user.username == settings.TEST_USER:
            return Response(settings.TEST_USER_DATA)
        raw_data = get_user_data(request)
        serializer = UserSerializer(raw_data)
        return Response(serializer.data)


class YearView(APIView):
    def get(self, request, format=None):
        if request.user and request.user.username == settings.TEST_USER:
            return Response(settings.TEST_YEAR_DATA)
        raw_data = get_year_data(request)
        serializer = YearSerializer(raw_data)
        return Response(serializer.data)


def logout_view(request):
    request.session.clear()
    return redirect("//log:out@{}/user/".format(request.get_host()))
