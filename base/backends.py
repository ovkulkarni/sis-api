from django.conf import settings
from django.core.cache import cache
from django.contrib import auth

from rest_framework import authentication, exceptions
from rest_framework.authentication import SessionAuthentication

from .management.commands.check_for_updates import FakeRequest
from .helpers import api_request, get_user_data
from .models import User


class SISAuthBackend(object):

    def authenticate(self, request, username=None, password=None):
        xml_data = api_request(username, password, "GetPXPMessages")
        if xml_data.find("RT_ERROR"):
            return None
        user, created = User.objects.get_or_create(username=username)
        if request.GET.get("save_password") or request.POST.get("save_password"):
            user.encrypted_password = settings.CIPHER.encrypt(password)
        else:
            user.encrypted_password = None
            request.session['password'] = password
        key = "{}:ChildList".format(user.username)
        if not cache.get(key):
            get_user_data(FakeRequest(user, password=password))
        user.save()
        return user


class SISBasicAuthentication(authentication.BasicAuthentication):

    def authenticate_credentials(self, userid, password, request):
        """Authenticate the userid and password."""

        user = auth.authenticate(request=request, username=userid, password=password)

        if user is None or (user and not user.is_active):
            raise exceptions.AuthenticationFailed("Invalid username/password.")

        return (user, None)
