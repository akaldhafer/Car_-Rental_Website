from os import name
from django.urls import path
from . import views


app_name = 'Home'

urlpatterns = [
    path('', views.home_pag ,name='home'),

]