# Generated by Django 5.0.6 on 2024-05-19 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softisepapp', '0006_remove_logiciel_cours'),
    ]

    operations = [
        migrations.AddField(
            model_name='logiciel',
            name='date_de_sortie',
            field=models.DateField(default=datetime.date(2002, 11, 10)),
        ),
        migrations.AddField(
            model_name='logiciel',
            name='systeme_exploitation',
            field=models.CharField(default='Windows', max_length=100),
        ),
        migrations.AddField(
            model_name='logiciel',
            name='version',
            field=models.CharField(default='1.0', max_length=50),
        ),
    ]
