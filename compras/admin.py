from django.contrib import admin
from .models import Category,Product
# Register your models here.


class CategoryAdm(admin.ModelAdmin):
    ...


class ProductAdm(admin.ModelAdmin):
    ...

admin.site.register(Product,ProductAdm)
admin.site.register(Category,CategoryAdm)