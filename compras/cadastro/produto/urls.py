from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_produto, name='cadastrar_produto'),
    path('create/', views.enviar_produto, name='enviar_produto'),
]