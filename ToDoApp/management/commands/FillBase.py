from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from ToDoApp.models import Task


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total_users', type=int, help='Indicates the number of users to be created')
        parser.add_argument('total_ToDo', type=int,
                            help='Specifies the number of records to create for each user')

    def handle(self, *args, **options):
        total_users = options['total_users']
        total_ToDo = options['total_ToDo']
        for i in range(total_users):
            User.objects.create_user(username=get_random_string(), email='', password='123')
        users = User.objects.all()
        for user in users:
            for i in range(total_ToDo):
                Task.objects.create(task_title=get_random_string(), task_author=user)
