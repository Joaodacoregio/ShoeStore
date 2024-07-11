from django.urls import path
from . import views

app_name = "compras"

urlpatterns = [
    path('',views.compras_home),
    path('produto/<int:id>',views.produto , name="product"),


    #Cadastros
    path('cadastro/marca' , views.cadastrar_marca , name="cadastrar_marca"),
    path('cadastro/categoria' , views.cadastrar_categoria, name="cadastrar_categoria"),


    #Query set https://docs.djangoproject.com/pt-br/3.2/ref/models/querysets/ (consultas)
    path('produto/marca/<int:marca_id>/',views.filtrar_marca , name="filtrar_marca"),
    path('produto/categoria/<int:categoria_id>',views.filtrar_categoria , name="filtrar_categoria"),
    path('produto/genero/<slug:genero>',views.filtrar_genero , name="filtrar_genero"),
    
    
]