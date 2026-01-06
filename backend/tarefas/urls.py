from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register(r'tarefas', views.TarefaViewSet) # cria rotas padroes - os metodos do crud com passagem de path param automaticamente

urlpatterns = [
  path('', views.get_all_tarefas, name='tarefas'),
  path('create/', views.create_tarefa, name='create_tarefa')
]
