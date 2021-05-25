from django.contrib import admin
from .models import Note,Assignment,Student_assign,Video,Pdf
# Register your models here.

admin.site.register(Note)
admin.site.register(Assignment)
admin.site.register(Student_assign)
admin.site.register(Video)
admin.site.register(Pdf)
