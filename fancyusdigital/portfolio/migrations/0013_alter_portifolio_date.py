# Generated by Django 4.2.3 on 2023-07-11 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_alter_portifolio_options_alter_portifolio_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portifolio',
            name='date',
            field=models.DateField(verbose_name='Post Date'),
        ),
    ]
