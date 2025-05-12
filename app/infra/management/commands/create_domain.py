# core/management/commands/create_domain.py

import os
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError

TEMPLATE_URLS = '''from django.urls import path
from domains.@@appname import views

urlpatterns = [
    # path('', views.index, name='index'),
]

'''

TEMPLATE_OPA = '''from functools import wraps
from ninja.errors import HttpError
from infra.security.opa_client import OPAClient

opa = OPAClient()

'''
# This is a sample function
# def opa_check(policy_path: str):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(request, *args, **kwargs):
#             input_data = {
#                 "user": str(request.user),
#                 "path": request.path,
#                 "method": request.method,
#                 "query": request.GET.dict(),
#             }
#             allowed = opa.evaluate_policy(policy_path, input_data)
#             if not allowed:
#                 raise HttpError(403, "Access Denied by OPA Policy")
#             return func(request, *args, **kwargs)
#         return wrapper
#     return decorator
    


TEMPLATE_TASKS = '''from celery import shared_task
import time
import logging

'''

# logger = logging.getLogger(__name__)

# @shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 3})
# def slow_addition(self, x, y):
#     """
#     Performs a slow addition, retrying on failure.
#     - bind=True allows access to self (task instance).
#     - autoretry_for handles automatic retries on exceptions.
#     - retry_backoff adds exponential delay between retries.
#     """
#     logger.info(f"Executing slow addition for {x} + {y}")
#     time.sleep(5)
#     return x + y


class Command(BaseCommand):
    help = 'Create a Django app inside the domains/ directory, with urls.py and without admin.py'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='The name of the domain app to create')

    def handle(self, *args, **options):
        app_name = options['name']
        base_path = Path('domains') / app_name

        if base_path.exists():
            raise CommandError(f"The app '{app_name}' already exists in domains/.")
        
        template = TEMPLATE_URLS.replace("@@appname", app_name)

        # Create base structure
        try:
            (base_path / 'migrations').mkdir(parents=True)
            (base_path / '__init__.py').touch()
            (base_path / 'apps.py').write_text(
                f"from django.apps import AppConfig\n\n\nclass {app_name.capitalize()}Config(AppConfig):\n    default_auto_field = 'django.db.models.BigAutoField'\n    name = 'domains.{app_name}'\n"
            )
            (base_path / 'models.py').write_text("from django.db import models\n")
            (base_path / 'views.py').write_text(f"from django.shortcuts import render\nfrom domains.{app_name}.opa import *\n")
            (base_path / 'tests.py').write_text("from django.test import TestCase\n")
            (base_path / 'urls.py').write_text(template)
            (base_path / 'opa.py').write_text("")
            (base_path / 'services.py').write_text(TEMPLATE_TASKS)
            (base_path / 'migrations' / '__init__.py').touch()
            
            # chatgpt add a way to RUN BLACK after create the domain

            self.stdout.write(self.style.SUCCESS(f"Domain app '{app_name}' created successfully in domains/"))
        except Exception as e:
            raise CommandError(f"Error creating domain app: {e}")

