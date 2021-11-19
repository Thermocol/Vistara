from os import name
from django.contrib import admin
from django.urls import path
from .views import Profileview


urlpatterns=[
    path('<int:pk>/', Profileview.as_view(), name='profile'),
    

]