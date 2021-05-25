from django import forms
from .models import Note2,Assignment2,Student_assign2,Video2,Pdf2
from datetime import datetime

class NoteForm2(forms.ModelForm):
    class Meta:
        model = Note2
        fields = ('subject_name','unit','topic','pdf','date')

class AssignmentForm2(forms.ModelForm):
    class Meta:
        model = Assignment2
        fields = ['subject_name','title', 'desc', 'image','date_posted','last_date']
        
class StudentassignForm2(forms.ModelForm):
    class Meta:
        model = Student_assign2
        fields = ['title','name', 'Roll_no','pdf','date']

class VideoUploadForm2(forms.ModelForm):
     class Meta:
         model = Video2
         fields = ['subject_name','caption','video','date']
        #  ordering = ['subject_name']

class UploadPdfForm2(forms.ModelForm):
    class Meta:
        model = Pdf2
        fields = ('subject_name','add_pdf')

