# Generated by Django 4.2.3 on 2023-07-11 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Portifolio',
        ),
        migrations.DeleteModel(
            name='PortifolioTag',
        ),
    ]
