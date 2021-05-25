from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    #we create fields that we want in our form here and in which order
    class Meta:
        model = CustomUser
        fields = [
        'is_student',
        'is_teacher',
        'Branch',
        'Year',
        'username',
        'first_name',
        'last_name',
        'phone_no',
        'email',
        'password1',
        'password2',
        'avatar',
        ]
        
        help_texts = {
            'username': None,
            'email': None,
            'password':None
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_no',
            'password1',
            'avatar',
            ] 
       

class ApprovalForm(forms.ModelForm):
   
    class Meta:
        model = CustomUser
        fields = ['is_approved']
        required= False
        
  
        