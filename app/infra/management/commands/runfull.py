import subprocess
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run makemigrations, migrate, and runserver in sequence"

    def add_arguments(self, parser):
        parser.add_argument(
            "--host",
            default="127.0.0.1",
            help="Host address to bind the server to (default: 127.0.0.1)",
        )
        parser.add_argument(
            "--port", default="8000", help="Port to bind the server to (default: 8000)"
        )

    def handle(self, *args, **options):
        host = options["host"]
        port = options["port"]

        try:
            self.stdout.write(self.style.NOTICE("Running makemigrations..."))
            subprocess.check_call(["python", "manage.py", "makemigrations"])

            self.stdout.write(self.style.NOTICE("Running migrate..."))
            subprocess.check_call(["python", "manage.py", "migrate"])

            self.stdout.write(
                self.style.NOTICE(
                    f"Starting development server at http://{host}:{port}/"
                )
            )
            subprocess.check_call(
                ["python", "manage.py", "runserver", f"{host}:{port}"]
            )

        except subprocess.CalledProcessError as e:
            self.stderr.write(self.style.ERROR(f"Command failed: {e}"))
