from django.db import models
from ..categoria.models import Category
from ..marca.models import Mark
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
import sys

COLOR_BASIC_CHOICES = [
    ('vermelho', 'Vermelho'),
    ('azul', 'Azul'),
    ('verde', 'Verde'),
    ('amarelo', 'Amarelo'),
    ('preto', 'Preto'),
    ('branco', 'Branco'),
]

GENDER_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    ]

class Product(models.Model):
 

    title = models.CharField(max_length=64)
    title_slug = models.SlugField(max_length=64,default="")
    gener = models.CharField(max_length=10, choices=GENDER_CHOICES)
    created_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    sale_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    cost_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    profit_margin = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    color = models.CharField(max_length=10, choices=COLOR_BASIC_CHOICES)
    reference = models.CharField(max_length=10,default="")
    size = models.IntegerField(default=0)

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


@receiver(pre_save, sender=Product)
def redimensionar_imagem(sender, instance, **kwargs):
    img = instance.img
    if img:
        img_temp = Image.open(img)
        #converte para RGB se for RGBA
        if img_temp.mode == 'RGBA':
            img_temp = img_temp.convert('RGB')
        output_io_stream = BytesIO()
        # Define a resolução fixa desejada (exemplo: 800x800)
        fixed_width, fixed_height = 600, 400
        img_temp = img_temp.resize((fixed_width, fixed_height))
        img_temp.save(output_io_stream, format='JPEG', quality=95)
        output_io_stream.seek(0)
        img_name = '{}.jpg'.format(img.name.split('.')[0])
        instance.img = InMemoryUploadedFile(output_io_stream, 'ImageField', img_name, 'image/jpeg', sys.getsizeof(output_io_stream), None)