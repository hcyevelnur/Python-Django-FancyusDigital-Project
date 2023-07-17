# Generated by Django 4.2.3 on 2023-07-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='upload/images', verbose_name='Şəkil Yerləşdir')),
                ('title', models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, verbose_name='Başlıq:')),
                ('description', models.TextField(verbose_name='Haqqında:')),
                ('client_name', models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, verbose_name='Client Name:')),
                ('date', models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, verbose_name='Date:')),
                ('website', models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, verbose_name='Website:')),
                ('category', models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, verbose_name='Category:')),
                ('title_1', models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, verbose_name='Başlıq:')),
                ('description_3', models.TextField(verbose_name='Haqqında:')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio',
            },
        ),
    ]
