from django.shortcuts import render

# Create your views here.
def parent_index(request):
    return render(request,'parenttemp/index.html')
def parent_chat(request):
    return render(request,'parenttemp/chat.html')    