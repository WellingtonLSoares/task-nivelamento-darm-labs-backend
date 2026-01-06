from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Tarefa
from .serializers import TarefaSerializer

import json

# Create your views here.
@api_view(['GET'])
def get_all_tarefas(request):
  tarefas = Tarefa.objects.all()
  serializer = TarefaSerializer(tarefas, many=True)

  return Response(serializer.data)


