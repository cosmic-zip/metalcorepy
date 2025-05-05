# core/management/commands/create_domain.py

import os
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError

TEMPLATE_URLS = '''from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
]
'''

class Command(BaseCommand):
    help = 'Create a Django app inside the domains/ directory, with urls.py and without admin.py'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='The name of the domain app to create')

    def handle(self, *args, **options):
        app_name = options['name']
        base_path = Path('domains') / app_name

        if base_path.exists():
            raise CommandError(f"The app '{app_name}' already exists in domains/.")

        # Create base structure
        try:
            (base_path / 'migrations').mkdir(parents=True)
            (base_path / '__init__.py').touch()
            (base_path / 'apps.py').write_text(
                f"from django.apps import AppConfig\n\n\nclass {app_name.capitalize()}Config(AppConfig):\n    default_auto_field = 'django.db.models.BigAutoField'\n    name = 'domains.{app_name}'\n"
            )
            (base_path / 'models.py').write_text("from django.db import models\n")
            (base_path / 'views.py').write_text("from django.shortcuts import render\n")
            (base_path / 'tests.py').write_text("from django.test import TestCase\n")
            (base_path / 'urls.py').write_text(TEMPLATE_URLS)
            (base_path / 'migrations' / '__init__.py').touch()

            self.stdout.write(self.style.SUCCESS(f"Domain app '{app_name}' created successfully in domains/"))
        except Exception as e:
            raise CommandError(f"Error creating domain app: {e}")

