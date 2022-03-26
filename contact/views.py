from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contact(request):

   myinfo = info.objects.first()
   if request.method == 'POST':
        subject = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
           message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
)

        print(subject, email, message)

  

   return render(request, './Cars/contant_us.html', {"myinfo":myinfo})






