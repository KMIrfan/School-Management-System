from django.shortcuts import render


# Create your views here.
def common_home(request):
    return render(request,'commontemp/home.html')
def common_index(request):
    return render(request,'commontemp/index.html')    
