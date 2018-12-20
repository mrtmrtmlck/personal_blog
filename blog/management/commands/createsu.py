from decouple import config
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = config('ADMIN_USERNAME')
        email = config('ADMIN_EMAIL')
        password = config('ADMIN_PASSWORD')
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
