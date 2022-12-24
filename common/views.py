from django.shortcuts import render

# Create your views here.
def common_index(request):
    return render(request,'commontemp/index.html')
