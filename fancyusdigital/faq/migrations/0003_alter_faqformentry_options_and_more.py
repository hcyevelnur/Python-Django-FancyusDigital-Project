# Generated by Django 4.2.3 on 2023-07-12 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_faqformentry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqformentry',
            options={'verbose_name': 'Faq form', 'verbose_name_plural': 'Faq form'},
        ),
        migrations.RemoveField(
            model_name='faqformentry',
            name='LastName',
        ),
    ]