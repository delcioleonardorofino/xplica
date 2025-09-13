from django.urls import path
from . import views

urlpatterns = [
    path('entrar/', views.entrar, name='entrar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sair/', views.sair, name='sair')
    
]