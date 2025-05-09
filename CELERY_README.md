# Configuração do Celery no Projeto

Este projeto utiliza o Celery para processamento de tarefas assíncronas e tarefas periódicas.

## Arquivos Configurados

- `core/celery.py`: configuração principal do Celery
- `core/__init__.py`: inicialização do app Celery com o Django
- `core/celery_beat.py`: configuração de tarefas periódicas
- `core/settings.py`: configurações do Celery adicionadas

## Como Usar

### Executar o Celery (desenvolvimento local)

1. Iniciar o Redis (se não estiver usando Docker):

```bash
redis-server
```

2. Iniciar o worker do Celery:

```bash
celery -A core worker --loglevel=info
```

3. Iniciar o Celery Beat para tarefas agendadas:

```bash
celery -A core beat --loglevel=info
```

### Usando Docker Compose

Execute todos os serviços juntos:

```bash
docker-compose up
```

## Criando Novas Tarefas

1. Crie um arquivo `tasks.py` em seu módulo Django:

```python
from celery import shared_task

@shared_task
def minha_tarefa(param1, param2):
    # Lógica da tarefa
    return resultado
```

2. Use a tarefa em seus views/controllers:

```python
from .tasks import minha_tarefa

# Execução assíncrona
resultado = minha_tarefa.delay(param1, param2)

# ou passando um tempo específico para execução (countdown em segundos)
resultado = minha_tarefa.apply_async(args=[param1, param2], countdown=60)
```

## Adicionar Novas Tarefas Periódicas

Para adicionar uma nova tarefa periódica, edite o arquivo `core/celery_beat.py`: 