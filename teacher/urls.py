
from django.urls import path
from .import views

app_name='teacher'

urlpatterns = [
 
    path('', views.teacher_index,name='index'),
    path('addmarks', views.teacher_addmarks,name='addmarks'),
    path('addtimetable', views.teacher_addtimetable,name='addtimetable'),
    path('addexamtimetable', views.teacher_addexamtimetable,name='addexamtimetable'),

]