from django.urls import path
from . import views



urlpatterns = [
    path('',views.compras_home),
    path('produto/<int:id>',views.produto),
    
]