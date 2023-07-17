# Generated by Django 4.2.3 on 2023-07-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, verbose_name='Başlıq:')),
                ('description', models.TextField(verbose_name='Haqqında:')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/images', verbose_name='Şəkil Yerləşdir')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='upload/images', verbose_name='Şəkil Yerləşdir')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Service',
            },
        ),
    ]