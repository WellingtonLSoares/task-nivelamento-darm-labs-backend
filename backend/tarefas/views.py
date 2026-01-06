from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


from .models import Tarefa
from .serializers import TarefaSerializer

import json

# Create your views here.
@api_view(['GET'])
def get_all_tarefas(request):
  tarefas = Tarefa.objects.all()
  serializer = TarefaSerializer(tarefas, many=True)

  return Response(serializer.data)

# class TarefaViewSet(viewsets.ModelViewSet):
  
#   queryset = Tarefa.objects.all().order_by('-created_at') # queryset e serializer_class são nomes padroes procurados pelo framework para criar os metodos padroes
#   serializer_class = TarefaSerializer

@api_view(['POST'])
def create_tarefa(request):
  new_tarefa = request.data

  serializer = TarefaSerializer(data=new_tarefa)

  if serializer.is_valid():
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
