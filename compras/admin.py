from django.contrib import admin
from .models import Category
# Register your models here.


class CategoryAdm(admin.ModelAdmin):
    ...

admin.site.register(Category,CategoryAdm)