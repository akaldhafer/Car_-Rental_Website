from os import name
from django.urls import path
from . import views


app_name = 'browsr_cars'

urlpatterns = [
    path('', views.All_car,name='all_cars'),
    path('<int:id>', views.car_detiles,name='car_detiles'),
    path('delete/<int:id>', views.car_delete,name='car_delete'),
    path('card/<int:id>', views.creat_order_and_send_emial,name='hi'),



]