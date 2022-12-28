from django.shortcuts import render

# Create your views here.
def parent_index(request):
    return render(request,'parenttemp/index.html')