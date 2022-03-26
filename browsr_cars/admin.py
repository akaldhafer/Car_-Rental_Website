from django.contrib import admin
from .models import Cars, Category, Order_car
# Register your models here.
admin.site.register(Cars)
admin.site.register(Category)
admin.site.register(Order_car)

