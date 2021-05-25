
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('',views.basic, name='basic'),
    path('search/',views.search, name='search'),
    path('sidebar/',views.sidebar,name='sidebar'),
    path('about/',views.about,name='about'),
    path('courses/',views.courses,name='courses'),
    path('editProfile/',views.editProfile,name='editProfile'),
    path('jitsimeet/',views.jitsimeet,name='jitsimeet'),
    path('meeting/',views.meeting,name='meeting'),
    path('Students_list/',views.Students_list,name='Students_list'),
    path('Teachers_list/',views.Teachers_list,name='Teachers_list'),
    path('basic/pendingreq/',views.pendingreq,name='pendingreq'),
]
