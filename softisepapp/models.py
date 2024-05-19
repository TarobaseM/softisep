from django.db import models
from datetime import date
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
    version = models.CharField(max_length=50,default="1.0")
    date_de_sortie = models.DateField(default=date(2002, 11, 10))
    systeme_exploitation = models.CharField(max_length=100,default="Windows")
    url_telechargement = models.URLField()
    
    def __str__(self):
        return self.nom
