
from django.urls import path,re_path
from django.conf.urls import url,include
from . import views as po_view

urlpatterns = [
    url(r'^$',po_view.index),
    path('dashboard',po_view.dashboard),
    path('signup',po_view.signup),
    path('login',po_view.login),
    path('logout',po_view.logout),
    path('portalusers',po_view.portal_users),
    path('userprofile',po_view.userprofile),
    path('kitchen',po_view.kitchen),
    path('kitchen_orders',po_view.kitchen_orders),
    path('kitchen_process',po_view.kitchen_process),
    path('testresult',po_view.testresult),
    path('usertestresultprofile',po_view.usertestresultprofile),
    path('medicine',po_view.medicine),
    path('addmedicine',po_view.addmedicine),
    path('medicine_deleted',po_view.medicine_deleted),
    path('medicine_update',po_view.medicine_update),
    path('med_save_update',po_view.med_save_update),
    path('mediorders',po_view.mediorders)


]