from django.shortcuts import render,redirect
from django.contrib import auth
#import pyautogui as pu
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from register.models import CustomUser

# Create your views here.
def login (request):
    if request.method =='POST':
        user1=request.POST.get('username')
        pass1=request.POST.get('password')
        
        user=auth.authenticate(username=user1,password=pass1)
        if user is not None:
            auth.login(request,user)
            if user.is_approved or user.is_superuser:
                if user.Year == '4th' and user.Branch == 'cse' or user.is_superuser:
                    return redirect('basic')
                else:
                    return HttpResponse('This page is not available')
            else:
                return redirect('approval')
        else:
            messages.error(request,f'Wrong Username or Password')
            return redirect('login')
        
    else:
        return render(request,'accounts/login.html')

def approval(request):
    return render(request,'accounts/approval.html')



