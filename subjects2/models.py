from django.db import models
from datetime import date

# Create your models here.
class Note2(models.Model):
    subject_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='notes/pdfs/')
    date = models.DateField(auto_now_add=False,auto_now=False,blank=True,help_text = "m/d/Y")

    def __str__(self):
        return self.unit
   

class Assignment2(models.Model):
    subject_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to='pics/')
    date_posted = models.DateField(auto_now_add=False,auto_now=False,blank=True,help_text = "m/d/Y")
    last_date = models.DateField(auto_now_add=False,auto_now=False,blank=True,help_text = "m/d/Y")
    
    def __str__(self):
        return self.title
   
    
class Student_assign2(models.Model):
    
    title=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    Roll_no = models.CharField(max_length=10)
    pdf = models.FileField(upload_to='notes/stu_pdfs/')
    date = models.DateField(auto_now_add=False,auto_now=False,blank=True,help_text = "m/d/Y")

    def __str__(self):
        return f'{self.name}'
    

class Video2(models.Model):
    subject_name=models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    date = models.DateField(auto_now_add=False,auto_now=False,blank=True,help_text = "m/d/Y")
    
    def __str__(self):
        return f'{self.subject_name}({self.caption})'

class Pdf2(models.Model):
    subject_name = models.CharField(max_length=100)
    add_pdf = models.FileField(upload_to='syllabi/')

    def __str__(self):
        return self.subject_name