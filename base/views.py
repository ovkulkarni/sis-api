from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, YearSerializer
from .helpers import get_user_data, get_year_data
# Create your views here.


class UserView(APIView):
    def post(self, request, format=None):
        raw_data = get_user_data(request)
        if raw_data.get("error"):
            return Response(raw_data)
        serializer = UserSerializer(raw_data)
        return Response(serializer.data)


class GradeView(APIView):
    def post(self, request, format=None):
        raw_data = get_year_data(request)
        if raw_data.get("error"):
            return Response(raw_data)
        serializer = YearSerializer(raw_data)
        return Response(serializer.data)
