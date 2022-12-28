from django.urls import path
from .import views

app_name='student'

urlpatterns = [
   
    path('', views.student_index,name='index'),
    path('leave', views.student_leave,name='leave'),

]