from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.registration),
	url(r'^validate/$', views.check_user, name="url_validate_user"),
]