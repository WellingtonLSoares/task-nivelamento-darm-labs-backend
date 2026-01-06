from django.db import models

# Create your models here.
class Tarefa(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField(blank=True, null=True)
  concluida = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.self.titulo
