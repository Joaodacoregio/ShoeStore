from django.contrib import admin
from  .cadastro.produto.models import Product
# Register your models here.


class CategoryAdm(admin.ModelAdmin):
    ...


class ProductAdm(admin.ModelAdmin):
    ...
    
admin.site.register(Product,ProductAdm)
 