from django.db import models

class Product(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    title = models.CharField(max_length=64)
    gener = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mark = models.CharField(max_length=32)
    created_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    #img = models.ImageField(upload_to='compras/img/%Y/%m/%d/')

class Shoes(Product):
  ...
 
