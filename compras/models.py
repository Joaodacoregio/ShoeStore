from django.db import models
#https://docs.djangoproject.com/pt-br/3.2/ref/models/fields/


class Category(models.Model):  
   name = models.CharField(max_length=16)

   def __str__(self) -> str:
      return self.name
   
class Mark(models.Model):  
   name = models.CharField(max_length=32)

   def __str__(self) -> str:
      return self.name

class Product(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    title = models.CharField(max_length=64)
    title_slug = models.SlugField(max_length=64,default="")
    gener = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
       to=Category,on_delete=models.SET_NULL,null=True
    )
    mark = models.ForeignKey(
       Mark,on_delete=models.SET_NULL,null=True
    )
    img = models.ImageField(upload_to='compras/img/%Y/%m/%d/')

    def __str__(self) -> str:
       return self.title

class Shoes(Product):
  ...
 
