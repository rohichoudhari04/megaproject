from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group



#for changing the look of admin panel 
class CustomAdmin(admin.ModelAdmin):
    #adding columns to the admin panel 
    list_display = ('username','first_name', 'last_name', 'email','is_approved')
    list_filter = [ 'is_teacher', 'is_student', 'is_superuser']

   
admin.site.register(CustomUser,CustomAdmin)
admin.site.unregister(Group)




