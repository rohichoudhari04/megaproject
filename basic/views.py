from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.shortcuts import get_object_or_404
from register.models import CustomUser
from register.forms import UserRegisterForm,EditProfileForm,ApprovalForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


@login_required
def basic(request):
    form = EditProfileForm(request.FILES,request.POST)
    if 'avatar' in request.FILES:
                profile_pic = request.FILES['avatar']
                request.user.avatar = profile_pic
                request.user.save()
                
    ur = CustomUser.objects.filter(is_approved = 'False',is_superuser='False').count()
    st = CustomUser.objects.filter(is_student='True').count()
    tt = CustomUser.objects.filter(is_teacher='True').count()
    context = { 'st':st, 'tt':tt,'ur':ur}
    return render(request,'profile/profile.html',context)


@login_required
def editProfile(request):  
    if request.method == 'POST':
        form = EditProfileForm(request.FILES,request.POST,instance=request.user)
        if form.is_valid():
                
                profile_pic = form.cleaned_data['avatar']
                request.user.avatar = profile_pic
                request.user.save()
                form.save(commit=False)
                messages.success(request,'Your Profile has been updated!')
                return redirect('basic')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'profile/editprofile.html',{'form': form} )



@login_required
def courses(request):
    return render(request,'basictemp/page.html')

@login_required
def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        people = CustomUser.objects.all().filter(first_name=search)
    else:
        search = None
    return render(request,'basictemp/search.html',{'people':people})


    
@login_required
def sidebar(request):
    return render(request,'basictemp/sidebar.html')

@login_required
def jitsimeet(request):
    return render(request,'jitsimeet.html')

@login_required
def meeting(request):
    return render(request,'basictemp/meeting.html')

@login_required
def pendingreq(request):
    ap = CustomUser.objects.all().filter(is_superuser=False)
    if request.method == 'POST':  
        form = ApprovalForm(request.POST or None,instance=request.user) 
        if form.is_valid():
            user = CustomUser.objects.get(is_approved=False) 
            user.is_approved = True
            user.save()
            subject = 'Welcome to Digilearn!'
            message= f'Hi {user.first_name}{user.last_name}, Your Account has been approved by the admin.Please login again.'
            from_email= settings.EMAIL_HOST_USER
            recipient = [user.email]
            send_mail(subject, message, from_email , recipient,fail_silently=False,)
            form.save()
            return redirect('pendingreq')
          
    else:
        
        form = ApprovalForm(instance=request.user)
    context = {'form':form,'ap':ap}
    return render(request,'accounts/pendingreq.html',context)



@login_required
def about(request):
    return render(request,'basictemp/about.html')

@login_required
def Students_list(request):
    user = CustomUser.objects.filter(is_student='True')
    return render(request,'basictemp/Studentslist.html',{'user':user})


@login_required
def Teachers_list(request):
    tt = CustomUser.objects.filter(is_teacher='True')
    return render(request,'basictemp/Teacherlist.html',{'tt':tt})


    
