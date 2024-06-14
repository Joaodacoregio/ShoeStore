from django.contrib import admin
from django.urls import path,include
from ShoeStore.views import home,test


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('sobre/',test)
]