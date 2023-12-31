# Generated by Django 4.2.3 on 2023-07-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0003_alter_faqformentry_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqpost',
            name='description_en',
            field=models.TextField(null=True, verbose_name='The answer:'),
        ),
        migrations.AddField(
            model_name='faqpost',
            name='description_es',
            field=models.TextField(null=True, verbose_name='The answer:'),
        ),
        migrations.AddField(
            model_name='faqpost',
            name='title_en',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Question:'),
        ),
        migrations.AddField(
            model_name='faqpost',
            name='title_es',
            field=models.CharField(help_text='Ümumi dəyər 255 olmalıdır!', max_length=255, null=True, verbose_name='Question:'),
        ),
    ]
