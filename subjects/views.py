from django.shortcuts import render,redirect
from django.contrib import messages
from.forms import NoteForm,AssignmentForm,StudentassignForm,VideoUploadForm,UploadPdfForm
from .models import Note, Assignment,Student_assign,Video,Pdf 
# Create your views here.

def video(request):
    video = Video.objects.all()
    # video = Video.objects.all().order_by('subject_name')
    return render(request,'7thsem/video/video.html',{'video':video})

def upload_video(request):
    form = VideoUploadForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Video uploaded!')
        return redirect('video')
    else:
        form = VideoUploadForm()
    return render(request,'7thsem/video/upload_video.html',{'form':form})

def assignment(request):
     assign = Assignment.objects.all()
     return render(request,'7thsem/assignment/submit_assign.html',{'assign': assign})

def studentlist(request):
    sta = Student_assign.objects.all() 
    return render(request,'7thsem/assignment/stu_assign.html',{'sta':sta})

def upload_assign(request):
    form = AssignmentForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Assignment uploaded!')
        return redirect('assignment')
    else:
        form = AssignmentForm()
    
    return render(request,'7thsem/assignment/upload_assign.html',{'form':form})

def notes(request):
    notes = Note.objects.all()
    return render(request,'7thsem/notes/notes_list.html',{'notes': notes})

def upload_notes(request):
    form = NoteForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Notes uploaded!')
        return redirect('notes')
    else:
        form = NoteForm()
    return render(request,'7thsem/notes/upload_notes.html', {'form':form})

def student_assign(request):
    form = StudentassignForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your assignment has been submitted!')
        return redirect('assignment')
    else: 
        form = StudentassignForm()
    return render(request,'7thsem/assignment/student_assign.html',{'form':form})

def delete_video(request,pk):
    if request.method =='POST':
        video = Video.objects.get(pk=pk)
        video.delete()
    return redirect('video')

def delete_notes(request,pk):
    if request.method =='POST':
        note = Note.objects.get(pk=pk)
        note.delete()
    return redirect('notes')

def delete_assign(request,pk):
    if request.method =='POST':
        a = Assignment.objects.get(pk=pk)
        a.delete()
    return redirect('assignment')

def syllabipdf(request):
    form = UploadPdfForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('syllabi')
    else:
        form =  UploadPdfForm()
    return render(request,'7thsem/syllabi/syllabipdf.html',{'form':form}) 

def syllabi(request):
    pdf = Pdf.objects.all()
    return render(request,'7thsem/syllabi/syllabi.html',{'pdf':pdf})

def delete_pdf(request,pk):
    if request.method =='POST':
        dpdf = Pdf.objects.get(pk=pk)
        dpdf.delete()
    return redirect('syllabi')    
    