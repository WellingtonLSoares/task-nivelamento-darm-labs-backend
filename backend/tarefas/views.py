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

@api_view(['POST', 'GET'])
def create_tarefa(request):
  new_tarefa = request.data

  serializer = TarefaSerializer(data=new_tarefa)

  serializer.is_valid(raise_exception=True)
  serializer.save()

  return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_tarefa_by_id(request, id):
  try:
    tarefa = Tarefa.objects.get(id=id)

  except Tarefa.DoesNotExist:
    return Response(
      {
        "erro": "Tarefa não encontrada",
        "mensagem": f"Não existe nenhuma tarefa com o id {id}. Verifique o número digitado."
      },
      status=status.HTTP_404_NOT_FOUND
    )

  # Se achou, serializa e retorna
  serializer = TarefaSerializer(tarefa)

  return Response(serializer.data)
