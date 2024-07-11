from django.urls import path
from . import views

app_name = "compras"

urlpatterns = [
    path('',views.compras_home),
    path('produto/<int:id>',views.produto , name="product"),


    #Cadastros
    path('cadastro/marca' , views.cadastrar_marca , name="cadastrar_marca"),
    path('cadastro/categoria' , views.cadastrar_categoria, name="cadastrar_categoria"),


    #filtros
    path('produto/marca/<int:marca_id>/',views.filtrar_marca , name="filtrar_marca"),
    path('produto/categoria/<int:categoria_id>',views.filtrar_categoria , name="filtrar_categoria"),
    
]