from django.shortcuts import render


# Create your views here.
def student_index(request):
    return render(request,'studenttemp/index.html')
def student_leave(request):
    return render(request,'studenttemp/leave.html')    