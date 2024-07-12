from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_marca, name='cadastrar_marca'),
]