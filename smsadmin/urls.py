
from django.urls import path
from .import views

app_name='smsadmin'

urlpatterns = [
 
    path('', views.smsadmin_index,name='index'),

]