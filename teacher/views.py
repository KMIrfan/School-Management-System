from django.shortcuts import render


# Create your views here.
def teacher_index(request):
    return render(request,'teachtemp/index.html')
def teacher_addmarks(request):
    return render(request,'teachtemp/addmarks.html') 
def teacher_addtimetable(request):
    return render(request,'teachtemp/addtimetable.html')   
def teacher_addexamtimetable(request):
    return render(request,'teachtemp/addexamtimetable.html')     