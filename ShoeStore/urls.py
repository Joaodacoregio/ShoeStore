from django.contrib import admin
from django.urls import path,include
from ShoeStore.views import home,contato



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('contato/',contato)
 
]