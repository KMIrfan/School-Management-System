from django.shortcuts import render

# Create your views here.
def smsadmin_index(request):
    return render(request,'smsadmintemp/index.html')