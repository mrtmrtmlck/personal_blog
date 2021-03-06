from decouple import config
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username=config('ADMIN_USERNAME')).exists():
            User.objects.create_superuser(config('ADMIN_USERNAME'), config('ADMIN_EMAIL'), config('ADMIN_PASSWORD'))
