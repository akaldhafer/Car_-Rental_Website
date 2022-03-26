from django.shortcuts import render
from .models import worker_info
from django.core.paginator import Paginator

# Create your views here.

def All_employds(request):

   all_car = worker_info.objects.all()

   paginator = Paginator(all_car, 8)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   context = {'all':page_obj}

   return render(request, './Cars/about_team.html', context)




def car_employds(request, id):
    job_lists = worker_info.objects.get(id=id)
    all_car = worker_info.objects.all()


    return render(request, './Cars/profile.html', {'all':job_lists, 'all_car':all_car})




