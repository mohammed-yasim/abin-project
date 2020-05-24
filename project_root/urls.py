from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
from project_admin.views import api,payment_gen,checkout,payment_success
from project_admin.views import profile_api
admin.site.site_header = "Break The Chain"
admin.site.site_title = "Break The Chain"
admin.site.index_title = "Welcome to Break The Chain Dashboard"

urlpatterns = [
    url(r'^',include('home.urls')),
    path('portal/',include('portal.urls')),
    path('portal_official/',include('portal_official.urls')),
    path('covid-test/',include('covid_test.urls')),
    path('super-admin/', admin.site.urls),
    path('api/<str:query>',api),
    path('profile_api/<str:query>',profile_api),
    path('payment_gateway/',payment_gen),
    path('payment_gateway/checkout/',checkout),
    path('payment_gateway/payment_success/',payment_success)
    
]
