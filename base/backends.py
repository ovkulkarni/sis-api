from django.conf import settings
from django.contrib import auth

from rest_framework import authentication, exceptions
from rest_framework.authentication import SessionAuthentication

from .helpers import api_request
from .models import User


class SISAuthBackend(object):

    def authenticate(self, request, username=None, password=None):
        xml_data = api_request(username, password, "GetPXPMessages")
        if xml_data.find("RT_ERROR"):
            return None
        user, created = User.objects.get_or_create(username=username,
                                                   defaults={'firebase_device_id': request.GET.get("firebase_device_id", "")})
        if request.GET.get("save_password"):
            user.encrypted_password = settings.CIPHER.encrypt(password)
        else:
            request.session['password'] = password
        if user.firebase_device_id != request.GET.get("firebase_device_id", ""):
            user.firebase_device_id = request.GET.get("firebase_device_id", "")
        user.save()
        return user


class SISBasicAuthentication(authentication.BasicAuthentication):

    def authenticate_credentials(self, userid, password, request):
        """Authenticate the userid and password."""

        user = auth.authenticate(request=request, username=userid, password=password)

        if user is None or (user and not user.is_active):
            raise exceptions.AuthenticationFailed("Invalid username/password.")

        return (user, None)
