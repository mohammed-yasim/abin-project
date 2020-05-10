
from django.urls import path,re_path
from django.conf.urls import url,include
from .views import corona,coronagetresult


urlpatterns = [
    path('',corona),
    path('result',coronagetresult)
    
]