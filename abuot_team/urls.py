from django.urls import path
from . import views


app_name = 'abuot_team'

urlpatterns = [
    path('', views.All_employds,name='All_employds'),
    path('<int:id>', views.car_employds,name='car_employds'),

]