from os import name
from django.contrib import admin
from django.db.models.indexes import Index
from django.http import request
from django.urls import path
from .views import createvideo, delvid, updatevid,index
from .views import index, detailvid


urlpatterns=[
    path('',index.as_view(),name='index'),
    path('create/',createvideo.as_view(),name='video-create'),
    path('<int:pk>/',detailvid.as_view(),name='Video-detail'),
    path('<int:pk>/update',updatevid.as_view(),name='video-update'),
    path('<int:pk>/delete',delvid.as_view(),name='video-delete'),

]