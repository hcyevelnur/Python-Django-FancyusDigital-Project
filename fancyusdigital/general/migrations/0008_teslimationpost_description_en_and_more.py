# Generated by Django 4.2.3 on 2023-07-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_emailadressfrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='teslimationpost',
            name='description_en',
            field=models.TextField(null=True, verbose_name='The answer:'),
        ),
        migrations.AddField(
            model_name='teslimationpost',
            name='description_es',
            field=models.TextField(null=True, verbose_name='The answer:'),
        ),
        migrations.AddField(
            model_name='teslimationpost',
            name='name_en',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Name:'),
        ),
        migrations.AddField(
            model_name='teslimationpost',
            name='name_es',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Name:'),
        ),
        migrations.AddField(
            model_name='teslimationpost',
            name='work_en',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Work:'),
        ),
        migrations.AddField(
            model_name='teslimationpost',
            name='work_es',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Work:'),
        ),
    ]
