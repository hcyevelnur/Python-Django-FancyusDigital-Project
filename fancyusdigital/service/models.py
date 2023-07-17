from django.db import models
from fancyusdigital.utils.base import BaseModel
from django.utils.html import format_html
# Create your models here.

class ServicePost(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Başlıq:', help_text='Ümumi dəyər 255 olmalıdır!')
    description = models.TextField( verbose_name='Haqqında:')
    description2 = models.TextField( verbose_name='Haqqında:')
    image_1 = models.ImageField(upload_to='upload/images', null=True, blank=True, verbose_name='Şəkil Yerləşdir')
    image = models.ImageField(upload_to='upload/images', null=True, blank=True, verbose_name='Icon Yerləşdir')
    image2 = models.ImageField(upload_to='upload/images', null=True, blank=True, verbose_name='Icon Yerləşdir')
    title_1 = models.CharField(max_length=255, verbose_name='Başlıq:', help_text='Ümumi dəyər 255 olmalıdır!')
    description_3 = models.TextField(verbose_name='Haqqında:')
    title_2 = models.CharField(max_length=255, verbose_name='Başlıq:', help_text='Ümumi dəyər 255 olmalıdır!')
    description_4 = models.TextField(verbose_name='Haqqında:')
    title_3 = models.CharField(max_length=255, verbose_name='Başlıq:', help_text='Ümumi dəyər 255 olmalıdır!')
    description_5 = models.TextField(verbose_name='Haqqında:')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Service'

    def __str__(self):
        return self.title
