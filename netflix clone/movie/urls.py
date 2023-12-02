from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='indexPage'),
    path('filmler/<int:id>',filmler,name='filmlerPage'),
]
