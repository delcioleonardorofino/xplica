from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('simulados/', views.simulados, name='simulados')
]
