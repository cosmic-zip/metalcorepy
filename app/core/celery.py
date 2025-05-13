import os
from celery import Celery

# Define o módulo de configurações padrão do Django para o Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Cria uma instância do Celery
app = Celery("core")

# Configuração usando as configurações do Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-descoberta de tarefas nos aplicativos instalados
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
