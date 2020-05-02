from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
from project_admin.views import api
from project_admin.views import profile_api

urlpatterns = [
    url(r'^',include('home.urls')),
    path('portal/',include('portal.urls')),
    path('portal_official/',include('portal_official.urls')),
    path('covid-test/',include('covid_test.urls')),
    path('super-admin/', admin.site.urls),
    path('api/<str:query>',api),
    path('profile_api/<str:query>',profile_api)
]
