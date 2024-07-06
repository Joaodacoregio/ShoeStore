from django.urls import path
from .views import compras_home
urlpatterns = [
    path('',compras_home),
]