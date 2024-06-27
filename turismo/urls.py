from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('editar/<int:servicio_id>/', views.editar, name='editar'),
]