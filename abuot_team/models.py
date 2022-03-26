from django.db import models

# Create your models here.
car_status = (
            ('New', 'new'),
            ('used', 'used'),
            )
option_work = (
            ('full time', 'full time'),
            ('part time', 'part time'),
            )


class worker_info (models.Model):

    
    name = models.CharField(max_length=10)
    email = models.EmailField( max_length=254)
    option_time_work = models.CharField(max_length=10,  choices=option_work)
    loction = models.CharField(max_length=30)
    time_start_work = models.DateField( default=0)
    namber_of_phone = models.CharField(max_length=100)
    disc = models.CharField(max_length=200)
    images = models.ImageField( upload_to='worker_imges')
    abuot_worker = models.CharField(max_length=100)
    published_at = models.DateField(auto_now=True)
    facebook = models.CharField(max_length=100, null=True)
    Twitter = models.CharField(max_length=100, null=True)
    Experience = models.CharField(max_length=5, null=True)
    stars = models.CharField(max_length=5, null=True)

    


    def __str__(self):
        return self.name 
