
from django.urls import path
from .import views

app_name='common'

urlpatterns = [
    path('home', views.common_home, name='home'),
    path('', views.common_index,name='index'),

]