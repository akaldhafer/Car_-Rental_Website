from django.shortcuts import render
from browsr_cars.models import Category# Create your views here.
def home_pag(request):
    all_datas = Category.objects.all()
    print(all_datas)

    

    return render(request, './Cars/index.html', {'all':all_datas})

    