from django.contrib import admin
from .models import Tarefa

# Register your models here.
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Tarefa._meta.fields]
  list_filter = ('concluida',)
  search_fields = ('titulo', 'descricao')
