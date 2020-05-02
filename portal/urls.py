
from django.urls import path,re_path
from django.conf.urls import url,include
from . import views as portal_views


urlpatterns = [
    url(r'^$',portal_views.index,name="Poral Home"),
    url(r'dashboard',portal_views.dashboard),
    url(r'logout',portal_views.logout),
    path('auth',portal_views.auth),
    path('q/<str:query>',portal_views.queries),
    path('save_profile',portal_views.profile_save)
]