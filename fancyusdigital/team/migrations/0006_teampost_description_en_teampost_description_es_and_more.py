# Generated by Django 4.2.3 on 2023-07-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampost',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Haqqında:'),
        ),
        migrations.AddField(
            model_name='teampost',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Haqqında:'),
        ),
        migrations.AddField(
            model_name='teampost',
            name='name_en',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Name:'),
        ),
        migrations.AddField(
            model_name='teampost',
            name='name_es',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Name:'),
        ),
        migrations.AddField(
            model_name='teampost',
            name='service_support_en',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Service Support:'),
        ),
        migrations.AddField(
            model_name='teampost',
            name='service_support_es',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Service Support:'),
        ),
        migrations.AddField(
            model_name='teampost',
            name='work_en',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Work:'),
        ),
        migrations.AddField(
            model_name='teampost',
            name='work_es',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Work:'),
        ),
    ]
