from django.urls import path
from . import views

app_name = "compras"

urlpatterns = [
    path('',views.compras_home),
    path('produto/<int:id>',views.produto , name="product"),
    
]