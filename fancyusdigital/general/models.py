from django.db import models
from fancyusdigital.utils.base import BaseModel
from django.utils.html import format_html
# Create your models here.


class TeslimationPost(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name:', help_text='Ümumi dəyər 255 olmalıdır!')
    work = models.CharField(max_length=255, verbose_name='Work:', help_text='Ümumi dəyər 255 olmalıdır!')
    description = models.TextField(verbose_name='The answer:')
    image_1 = models.ImageField(upload_to='upload/images', null=True, blank=True, verbose_name='Şəkil Yerləşdir')

    class Meta:
        verbose_name = 'Teslimation'
        verbose_name_plural = 'Teslimation'

    def __str__(self):
        return self.name


class ContactFormEntry(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    EmailAddress = models.EmailField()
    PhoneNo = models.CharField(max_length=255)
    Message = models.TextField()

    class Meta:
        verbose_name = 'Contact form'
        verbose_name_plural = 'Contact form'
        
    def __str__(self):
        return self.FirstName


class EmailAdressFrom(models.Model):
    EmailAddress = models.EmailField()

    class Meta:
        verbose_name = 'Email Address'
        verbose_name_plural = 'Email Address'
        
    def __str__(self):
        return self.EmailAddress