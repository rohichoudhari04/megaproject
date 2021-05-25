from django.shortcuts import render,redirect
from django.contrib import messages 
from .forms import UploadPdfForm2,NoteForm2,AssignmentForm2,StudentassignForm2,VideoUploadForm2
from .models import Pdf2,Note2, Assignment2,Student_assign2,Video2
# Create your views here.

# def subjects2(request):
#     return render(request,'8thsem/subjects2.html')

def studentlist2(request):
    sta = Student_assign2.objects.all() 
    return render(request,'8thsem/assignment/stu_assign2.html',{'sta':sta})

def video2(request):
    video = Video2.objects.all()
    return render(request,'8thsem/video/video2.html',{'video':video})

def upload_video2(request):
    form = VideoUploadForm2(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Video uploaded!')
        return redirect('video2')
    else:
        form = VideoUploadForm2()
    return render(request,'8thsem/video/upload_video2.html',{'form':form})

def assignment2(request):
     assign = Assignment2.objects.all()
     return render(request,'8thsem/assignment/submit_assign2.html',{'assign': assign})

def upload_assign2(request):
    form = AssignmentForm2(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Assignment uploaded!')
        return redirect('assignment2')
    else:
        form = AssignmentForm2()
    
    return render(request,'8thsem/assignment/upload_assign2.html',{'form':form})

def student_assign2(request):
    form = StudentassignForm2(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your assignment has been submitted!')
        return redirect('assignment')
    else: 
        form = StudentassignForm2()
    return render(request,'8thsem/assignment/student_assign2.html',{'form':form})

def notes2(request):
    notes = Note2.objects.all()
    return render(request,'8thsem/notes/notes_list2.html',{'notes': notes})

def upload_notes2(request):
    form = NoteForm2(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request,'Notes uploaded!')
        return redirect('notes2')
    else:
        form = NoteForm2()
    return render(request,'8thsem/notes/upload_notes2.html', {'form':form})

def delete_notes2(request,pk):
    if request.method =='POST':
        note = Note2.objects.get(pk=pk)
        note.delete()
    return redirect('notes2')

def delete_video2(request,pk):
    if request.method =='POST':
        video = Video2.objects.get(pk=pk)
        video.delete()
    return redirect('video2')


def delete_assign2(request,pk):
    if request.method =='POST':
        a = Assignment2.objects.get(pk=pk)
        a.delete()
    return redirect('assignment2')

def syllabi2(request):
    pdf = Pdf2.objects.all()
    return render(request,'8thsem/syllabi/syllabi2.html',{'pdf':pdf})

def syllabipdf2(request):
    form = UploadPdfForm2(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('syllabi2')
    else:
        form = UploadPdfForm2()
    return render(request,'8thsem/syllabi/syllabipdf2.html',{'form':form})

def delete_pdf2(request,pk):
    if request.method =='POST':
        dpdf = Pdf2.objects.get(pk=pk)
        dpdf.delete()
    return redirect('syllabi2') 