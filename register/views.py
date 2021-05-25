from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import CustomUser


# We removed usercreationform replacing it with our userRegisterform
# Create your views here.


def register(request):
    if request.method == 'POST':
         # if this is a POST request we need to process the form data
        form = UserRegisterForm(request.POST or None,request.FILES)
        user = CustomUser.objects.get(pk=1)
        # check whether it's valid:
        if form.is_valid():
            if user.is_teacher==True:
                user = CustomUser.objects.get(pk=1)
                profile_pic = form.cleaned_data['avatar']
                user.avatar = profile_pic
                user.save()
                # group = Group.objects.get(name='teacher')     
                # user.groups.add(group)
            else:
                user.is_student==True
                user = CustomUser.objects.get(pk=1)
                profile_pic = form.cleaned_data['avatar']
                user.avatar = profile_pic
                user.save()
                # group = Group.objects.get(name='student')
                # user.groups.add(group)
            
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
        
    return render(request, 'accounts/register.html',{'form':form})

    


