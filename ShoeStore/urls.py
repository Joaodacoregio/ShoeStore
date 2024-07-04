from django.contrib import admin
from django.urls import path,include
from ShoeStore.views import home,vendas



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('vendas/',vendas)
]