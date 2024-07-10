from django.db.models.signals import pre_save
from compras.models import Product
from django.dispatch import receiver
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
import sys



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