from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates admin with no validation. Input <username> <password> <repeat password>'
    
    def add_arguments(self, parser):
        parser.add_argument('admin_name', type=str, required=True, help='Username for admin')
        parser.add_argument('admin_password', type=str, required=True, help='Password for admin')
        parser.add_argument('admin_password_repeat', type=str, required=True, help='Password repeat')

    
    def handle(self, *args, **kwargs):
        name = kwargs['admin_name']
        password = kwargs['admin_password']
        repeat_password = kwargs['admin_password_repeat']
        
        if not password == repeat_password:
            raise CommandError('Different passwords, try again')

        if User.objects.filter(username=name).count() > 0:
            raise CommandError('This username already exists, try again')

        user=User.objects.create_user(name, password=password)
        user.is_superuser=True
        user.is_staff=True
        user.save()