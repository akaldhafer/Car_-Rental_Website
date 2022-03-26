from cmath import phase
from django.shortcuts import render, redirect
from .models import Cars, Order_car
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
import threading
# Create your views here.





def All_car(request):

   all_car = Cars.objects.all()

   paginator = Paginator(all_car, 9)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   context = {'all':page_obj}

   return render(request, './Cars/Browse_carsn.html', context)




def car_detiles(request, id):

   

    job_lists = Cars.objects.get(id=id)
    all_car = Cars.objects.all()

   


    return render(request, './Cars/car_detelis.html', {'all':job_lists, 'all_car':all_car})



@csrf_exempt
def creat_order_and_send_emial(request, id):

    job_lists = Cars.objects.get(id=id)
   




    def tasks():


        if request.method == "POST":

            frist_name = request.POST.get("first_name")
            last_name = request.POST.get('last_name')
            Email_ = request.POST.get('email')
            area_code = request.POST.get('area_code')
            Phone = request.POST.get('phone')
            selected =  request.POST.get('subject')
            checked = request.POST.get('exist')

            Order_car.objects.create(

                frist_name=frist_name,
                last_name = last_name,
                Email = Email_,
                selected = selected,
                checked = checked,
                phone = Phone +area_code,

                )

            info = (frist_name, last_name, Email_, area_code, selected, checked)


            send_mail (

                info,
                'this masseg from dev_arb combony',
                settings.EMAIL_HOST_USER,
                [Email_],


                     )
           

    print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;')



    t = threading.Thread(target=tasks)
    t.setDaemon(True)
    t.start()
    if request.method == "POST":
        return redirect('/')
    
 
  
    print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;')
    #print(frist_name, last_name, selected_car, Email_, area_code, selected, checked)
    

    return render(request,  './Cars/form_d.html',  {'all':job_lists})



def car_delete(request, id):
       
    job_lists = Cars.objects.get(id=id)
    if request.method == "POST":
         job_lists.delete()
         return redirect('cars:all_cars')
         

    return render(request, './Cars/delet.html', {'all':job_lists})





