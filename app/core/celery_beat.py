from celery.schedules import crontab

# Definição de tarefas periódicas
# Referência: https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
CELERY_BEAT_SCHEDULE = {
    # Executa a tarefa de limpeza de notificações todos os dias às 3 da manhã
    'cleanup-old-notifications-daily': {
        'task': 'modules.notification.tasks.cleanup_old_notifications',
        'schedule': crontab(hour=3, minute=0),
        'kwargs': {'days': 30},
    },
    # Exemplo de tarefa que executa a cada 30 minutos
    # 'task-name': {
    #     'task': 'app.module.tasks.function_name',
    #     'schedule': 30 * 60,  # 30 minutos em segundos
    # },
} 
