from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.subjects2,name='subjects2'),
    path('',views.video2, name='video2'),
    path('8thsem/uploadvideo2/',views.upload_video2,name='upload_video2'),
    path('8thsem/delete_video2/<int:pk>/',views.delete_video2,name='delete_video2'),
    path('8thsem/assignment2/',views.assignment2, name='assignment2'),
    path('8thsem/upload_assign2/',views.upload_assign2, name='upload_assign2'),
    path('8thsem/delete_assign2/<int:pk>/',views.delete_assign2,name='delete_assign2'),
    path('8thsem/student_assign2',views.student_assign2,name='student_assign2'),
    path('8thsem/notes2/',views.notes2, name='notes2'),
    path('8thsem/upload_notes2/',views.upload_notes2,name='upload_notes2'),
    path('8thsem/delete_notes2/<int:pk>/',views.delete_notes2,name='delete_notes2'),
    path('8thsem/studentlist2/',views.studentlist2,name='studentlist2'),
    path('8thsem/syllabi2/',views.syllabi2,name='syllabi2'),
    path('8thsem/syllabipdf2/',views.syllabipdf2,name='syllabipdf2'),
    path('8thsem/delete_pdf2/<int:pk>/',views.delete_pdf2,name='delete_pdf2'),
    
]
