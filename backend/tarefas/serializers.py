from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tarefa
    fields = '__all__'

    extra_kwargs = {
      'titulo': {
        'error_messages': {
          'blank': 'O título não pode ficar vazio, por favor preencha.',
          'required': 'O campo título é obrigatório no JSON.',
          'max_length': 'Ops! O título é muito longo. O limite é de 100 caracteres.'
        },
        'help_text': 'Insira um título curto e objetivo (máx. 100 caracteres).',
      },
      'descricao': {
        'error_messages': {
          'blank': 'A descrição não pode ficar vazio, por favor preencha.',
          'required': 'O campo descrição é obrigatório no JSON.'
        },
        'help_text': 'Descreva os detalhes da tarefa (opcional).',
      },
      'concluida': {
        'error_messages': {
          'invalid': 'Valor inválido! Por favor envie true ou false (booleano).',
          'null': 'Este campo não pode ser nulo.'
        },
        'help_text': 'Define se a tarefa foi finalizada ou não.',
      }
    }
