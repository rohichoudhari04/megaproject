from django import forms
from .models import Note,Assignment,Student_assign,Video,Pdf


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('subject_name','unit','topic','pdf','date')

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject_name','title', 'desc', 'image','date_posted','last_date']
        
class StudentassignForm(forms.ModelForm):
    class Meta:
        model = Student_assign
        fields = ['title','name', 'Roll_no','pdf','date']

class VideoUploadForm(forms.ModelForm):
     class Meta:
         model = Video
         fields = ['subject_name','caption','video','date']
       
class UploadPdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ('subject_name','add_pdf',)

#format='%m/%d/%Y',



         