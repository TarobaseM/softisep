from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Cours(models.Model):
    """
    Modèle représentant un cours.
    """
    nom = models.CharField(max_length=100)
    description = models.TextField(default="lorem ipsum")
    logiciels = models.ManyToManyField('Logiciel', related_name='cours_logiciels')
    eleves = models.ManyToManyField(User, related_name='cours')

    def __str__(self):
        return self.nom

class Logiciel(models.Model):
    """
    Modèle représentant un logiciel.
    """
    nom = models.CharField(max_length=100)
    description = models.TextField(default="lorem ipsum")
    version = models.CharField(max_length=50, default="1.0")
    date_de_sortie = models.DateField(default=date(2002, 11, 10))
    systeme_exploitation = models.CharField(max_length=100, default="Windows")
    url_telechargement = models.URLField()

    def __str__(self):
        return self.nom
