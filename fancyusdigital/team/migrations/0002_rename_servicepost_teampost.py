# Generated by Django 4.2.3 on 2023-07-11 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServicePost',
            new_name='TeamPost',
        ),
    ]