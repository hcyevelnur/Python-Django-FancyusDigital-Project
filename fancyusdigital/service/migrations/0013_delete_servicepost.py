# Generated by Django 4.2.3 on 2023-07-09 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_alter_servicepost_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServicePost',
        ),
    ]