# Generated by Django 4.2.3 on 2023-07-09 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0006_delete_servicepost_delete_servicepostelave'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePostElave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=25, verbose_name='Əlavə məlumat: ')),
                ('description', models.TextField(verbose_name='Haqqında:')),
                ('title_2', models.CharField(max_length=25, verbose_name='Əlavə məlumat: ')),
                ('description_2', models.TextField(verbose_name='Haqqında:')),
                ('title_3', models.CharField(max_length=25, verbose_name='Əlavə məlumat: ')),
                ('description_3', models.TextField(verbose_name='Haqqında:')),
            ],
            options={
                'verbose_name': 'Service Elave',
                'verbose_name_plural': 'Service Elave',
            },
        ),
        migrations.CreateModel(
            name='ServicePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, verbose_name='Başlıq:')),
                ('description', models.TextField(verbose_name='Haqqında:')),
                ('description2', models.TextField(verbose_name='Haqqında:')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='upload/images', verbose_name='Şəkil Yerləşdir')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/images', verbose_name='Icon Yerləşdir')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='upload/images', verbose_name='Icon Yerləşdir')),
                ('title_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elavemelumat', to='service.servicepostelave', verbose_name='Əlavə məlumat:')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Service',
            },
        ),
    ]
