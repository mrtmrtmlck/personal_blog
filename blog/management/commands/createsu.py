from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(os.environ.get('ADMIN_USERNAME'), os.environ.get('ADMIN_EMAIL'),
                                          os.environ.get('ADMIN_PASSWORD'))
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
