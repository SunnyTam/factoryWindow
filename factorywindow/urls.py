"""factorywindow URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views # let django handle login and authentication
from home import views as home_views
from factory import views as factory
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'redirect_authenticated_user': True, }, name='login'),
	url(r'^register/', include("users.urls")),

#	url( r'^', include("factory.urls")),

	url(r'^home/', home_views.index),
	url(r'^factory/story/', factory.story),
	url(r'^contact/', factory.request_form),
	url(r'^results/', include("factory.urls")),
]
