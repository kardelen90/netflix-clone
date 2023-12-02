from django.urls import path
from .views import *
urlpatterns = [
    path('login/',login_request,name='loginPage'),
    path('register/',register_request,name='registerPage'),
    path('logout/',logout_request,name='logoutPage'),
    path('profil/',profil,name='profilPage'),
    path('profil-manage/<slug:slug>',profil_manage,name='managePage'),
]
