# Generated by Django 5.0.6 on 2024-05-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softisepapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='description',
            field=models.TextField(default='lorem ipsum'),
        ),
    ]