from django.urls import path
from .views import conversor_view, historico_view

urlpatterns = [
    path('', conversor_view, name='conversor'),
    path('historico/', historico_view, name='historico'),
]


#é para chamar o formulário de conversão