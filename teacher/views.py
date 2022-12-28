from django.shortcuts import render


# Create your views here.
def teacher_index(request):
    return render(request,'teachtemp/index.html')