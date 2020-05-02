
from django.urls import path,re_path
from django.conf.urls import url,include
from . import views as home_views
from . import custom_api as resources_api


urlpatterns = [
    url(r'^$',home_views.index,name="Home"),
    url(r'^home',home_views.index,name="Home"),
    path('home',home_views.index,name="Home"),
    url(r'^index.html',home_views.index,name="Home"),
    url(r'^about',home_views.about,name="About"),
    path('about',home_views.about,name="About"),
    url(r'^about.html',home_views.about,name="About"),


    path('newsapi.org',resources_api.get_news),
    path('mohfw.gov.in',resources_api.get_status),
]