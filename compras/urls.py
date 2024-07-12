from django.urls import path,include
from . import views

app_name = "compras"

urlpatterns = [
    path('',views.compras_home),
    path('produto/<int:id>',views.produto , name="product"),


    #Cadastros
    path('cadastro/marca/', include('compras.cadastro.marca.urls')),
    path('cadastro/categoria/', include('compras.cadastro.categoria.urls')),
    path('cadastro/produto/', include('compras.cadastro.produto.urls')),


    #Query set https://docs.djangoproject.com/pt-br/3.2/ref/models/querysets/ (consultas)
    path('produto/marca/<int:marca_id>/',views.filtrar_marca , name="filtrar_marca"),
    path('produto/categoria/<int:categoria_id>',views.filtrar_categoria , name="filtrar_categoria"),
    path('produto/genero/<slug:genero>',views.filtrar_genero , name="filtrar_genero"),
    
    
]