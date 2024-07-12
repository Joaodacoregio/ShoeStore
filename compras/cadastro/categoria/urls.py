from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_categoria, name='cadastrar_categoria'),
]