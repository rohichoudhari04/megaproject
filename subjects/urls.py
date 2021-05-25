from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.video, name='video'),
    path('7thsem/assignment/assignment/',views.assignment, name='assignment'),
    path('7thsem/assignment/upload_assign/',views.upload_assign, name='upload_assign'),
    path('7thsem/notes/notes/',views.notes, name='notes'),
    path('7thsem/studentlist/',views.studentlist,name='studentlist'),
    path('7thsem/notes/upload_notes/',views.upload_notes,name='upload_notes'),
    path('7thsem/delete_video/<int:pk>/',views.delete_video,name='delete_video'),
    path('7thsem/delete_notes/<int:pk>/',views.delete_notes,name='delete_notes'),
    path('7thsem/assignment/delete_assign/<int:pk>/',views.delete_assign,name='delete_assign'),
    path('7thsem/assignment/student_assign',views.student_assign,name='student_assign'),
    path('7thsem/video/uploadvideo/',views.upload_video,name='upload_video'),
    path('7thsem/syllabi/syllabi/',views.syllabi,name='syllabi'),
    path('7thsem/syllabi/syllabipdf/',views.syllabipdf,name='syllabipdf'),
    path('7thsem/delete_pdf/<int:pk>/',views.delete_pdf,name='delete_pdf'),
    
]
