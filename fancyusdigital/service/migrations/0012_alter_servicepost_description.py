# Generated by Django 4.2.3 on 2023-07-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_alter_servicepost_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepost',
            name='description',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, verbose_name='Haqqında:'),
        ),
    ]