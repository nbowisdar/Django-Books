from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a default superuser'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin12"
            )
            self.stdout.write(self.style.SUCCESS("Successfully created default superuser."))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists."))
