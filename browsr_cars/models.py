from django.db import models

# Create your models here.


car_status = (
            ('New', 'new'),
            ('used', 'used'),
            )
car_option = (
            ('full option', 'full option'),
            ('normal', 'normal'),
            )


class Cars (models.Model):

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    generation = models.CharField(max_length=50)
    start_of_prodetion = models.IntegerField( default=0)
    contry_prodetion = models.CharField(max_length=50)
    doors = models.IntegerField( default=0)
    colors = models.CharField(max_length=10)
    status = models.CharField(max_length=10,  choices=car_status)
    price = models.IntegerField(default=0)
    option = models.CharField(max_length=50, choices=car_option)
    namber_of_cylinder = models.IntegerField( default=0)
    power_of_push = models.IntegerField( default=0)
    high_speed = models.IntegerField( default=0)
    disc = models.CharField(max_length=200)
    published_at = models.DateField(auto_now=True)
    images = models.ImageField( upload_to='cars_imges')
    images_2 = models.ImageField( upload_to='cars_imges')
    images_3 = models.ImageField( upload_to='cars_imges')
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.model + " " + self.brand


class Order_car (models.Model):

    frist_name = models.CharField(null=True, max_length=100)
    last_name = models.CharField(null=True,max_length=50)
    Email= models.CharField(null=True,max_length=50)
    selected = models.CharField(null=True,max_length=10)
    checked = models.CharField(null=True,max_length=10)
    phone = models.CharField(null=True,max_length=10)
    published_at = models.DateField(null=True,auto_now=True)
  


    def __str__(self):
        return str(self.frist_name )



class Category(models.Model):

    name = models.CharField(max_length=25)
    images = models.ImageField( upload_to='cars_img')


    def __str__(self):

        return self.name