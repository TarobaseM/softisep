import random
from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate users with random data'

    def handle(self, *args, **kwargs):
        # Créer des groupes
        group1, _ = Group.objects.get_or_create(name='Professeurs')
        group2, _ = Group.objects.get_or_create(name='élèves')

        # Créer des utilisateurs aléatoires
        for i in range(51,101):
            username = f'user{i}'
            email = f'user{i}@example.com'
            password = 'password123'

            # Récupérer un utilisateur existant ou le créer s'il n'existe pas
            user,created = User.objects.get_or_create(username=username, defaults={'email': email, 'password': password})
            # Assigner les utilisateurs aux groupes
            if random.choice([True, False]):
                user.groups.add(group1)
            else:
                user.groups.add(group2)

            self.stdout.write(self.style.SUCCESS(f'User "{username}" created or updated'))
             # Donner le statut "staff" aux utilisateurs du groupe 1
            if group1 in user.groups.all():
                user.is_staff = True
                user.save()
                self.stdout.write(self.style.SUCCESS(f'User "{username}" is staff'))

        self.stdout.write(self.style.SUCCESS('Data population complete'))
