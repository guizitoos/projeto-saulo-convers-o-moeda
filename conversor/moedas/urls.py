from django.urls import path
from .views import conversor_view

urlpatterns = [
    path('', conversor_view, name='conversor'),
]

#é para chamar o formulário de conversão