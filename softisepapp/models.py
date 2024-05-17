from django.db import models

# Create your models here.
from django.db import models




class Cours(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(default="lorem ipsum")
    logiciels = models.ManyToManyField('Logiciel', related_name='cours_logiciels')

    def __str__(self):
        return self.nom


class Logiciel(models.Model):
    description = models.TextField(default="lorem ipsum")
    nom = models.CharField(max_length=100)
    url_telechargement = models.URLField()
    
    def __str__(self):
        return self.nom
