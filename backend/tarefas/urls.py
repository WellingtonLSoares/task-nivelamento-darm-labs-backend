from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_all_tarefas, name='get_all_tarefas'),
]
