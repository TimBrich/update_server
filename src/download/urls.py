from django.contrib import admin
from django.urls import re_path, path, include
from django.views.generic import ListView, DetailView

from django.conf import settings
from django.conf.urls.static import static

from download.views import *

urlpatterns = [
    re_path(r'^download&fname=(?P<fname>\w+.\w+)$', download),
    re_path(r'^getUpdateInfo&version=(?P<version>\d+)&name=(?P<name>\w+)', getUpdateInfo)
]
