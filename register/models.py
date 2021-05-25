from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class CustomUser(AbstractUser):
    branch=(
        ('cse','computer science engineering'),
        ('other','other'),
    )
    year=(
        ('1st','First year'),
        ('2nd','Second year'),
        ('3rd','Third year'),
        ('4th','Fourth year'),
    )
    
    Branch = models.CharField(max_length=70,choices=branch)
    Year = models.CharField(max_length=70,choices=year)
    is_student = models.BooleanField('student status',default = False)
    is_teacher = models.BooleanField('teacher status',default = False)
    username = models.CharField(max_length=70,unique=True)
    phone_no = models.CharField(max_length=10,validators=[RegexValidator(regex='^.{10}$', message='Enter valid mobile no', code='nomatch')])
    email = models.EmailField(max_length=70)
    password1 = models.CharField(max_length=32,validators=[MinLengthValidator(4)])
    password2 = models.CharField(max_length=32,validators=[MinLengthValidator(4)])
    avatar = models.ImageField(upload_to='images/avatars/', null=True, blank=True)
    is_approved = models.BooleanField('Approved status', default = False,blank=True)
    def __str__(self):
        return self.username

    

    



    



    

