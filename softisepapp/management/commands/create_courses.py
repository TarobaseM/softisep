import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from softisepapp.models import Cours, Logiciel

class Command(BaseCommand):
    help = 'Populate courses with random data'

    def handle(self, *args, **kwargs):
        # Créer quelques logiciels
        logiciels = []
        for i in range(10):
            logiciel, _ = Logiciel.objects.get_or_create(
                nom=f'Logiciel{i}',
                defaults={
                    'description': 'Un logiciel utile pour les cours',
                    'version': f'{random.randint(1, 10)}.{random.randint(0, 9)}',
                    'date_de_sortie': '2020-01-01',
                    'systeme_exploitation': random.choice(['Windows', 'macOS', 'Linux']),
                    'url_telechargement': 'http://example.com'
                }
            )
            logiciels.append(logiciel)
        
        # Récupérer tous les utilisateurs
        users = list(User.objects.all())

        # Créer 50 cours
        for i in range(50):
            nom_cours = f'Cours{i}'
            cours, created = Cours.objects.get_or_create(
                nom=nom_cours,
                defaults={'description': 'Un cours fascinant sur un sujet d\'ingénierie informatique'}
            )

            # Associer 2 à 5 logiciels aléatoires au cours
            cours_logiciels = random.sample(logiciels, k=random.randint(2, 5))
            for logiciel in cours_logiciels:
                cours.logiciels.add(logiciel)

            # Associer 5 à 20 utilisateurs aléatoires au cours
            cours_users = random.sample(users, k=random.randint(5, 20))
            for user in cours_users:
                cours.eleves.add(user)

            self.stdout.write(self.style.SUCCESS(f'Cours "{nom_cours}" created or updated'))

        self.stdout.write(self.style.SUCCESS('Course population complete'))
