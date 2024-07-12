from django.db import models




class Category(models.Model):  
   name = models.CharField(max_length=16)

   def __str__(self) -> str:
      return self.name
   
 