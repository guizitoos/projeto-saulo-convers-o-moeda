from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('moedas.urls')),
]

#para indicar que a rota da URL ta no urls.py de moedas