from django.db import models


class Mark(models.Model):  
   name = models.CharField(max_length=32)

   def __str__(self) -> str:
      return self.name