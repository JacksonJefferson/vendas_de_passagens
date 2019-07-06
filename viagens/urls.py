from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('passagem/', views.passagem_list),
    path('passagem/<int:passagem_id>', views.passagem_show),
    path('passagem/create/', views.passagem_form),
    path('veiculo/', views.veiculo_list),
    path('veiculo/<int:veiculo_id>', views.veiculo_show),
    path('veiculo/create/', views.veiculo_form),

]