"""sis_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from base.views import GradeView, RootView, UserView, YearView

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", RootView.as_view()),
    url(r"^user/$", UserView.as_view()),
    url(r"^quarters/$", YearView.as_view()),
    url(r"^grades/$", GradeView.as_view()),
    url(r"^grades/quarter/(?P<qnum>[0-9]+)/$", GradeView.as_view()),
    url(r"^grades/class/(?P<period>[0-9]+)/$", GradeView.as_view()),
]
