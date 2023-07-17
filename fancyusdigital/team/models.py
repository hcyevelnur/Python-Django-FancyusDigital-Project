from django.db import models
from fancyusdigital.utils.base import BaseModel
from django.utils.html import format_html
# Create your models here.

class TeamPost(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name:', help_text='Ümumi dəyər 255 olmalıdır!')
    work = models.CharField(max_length=255, verbose_name='Work:', help_text='Ümumi dəyər 255 olmalıdır!')
    description = models.TextField(verbose_name='Haqqında:')
    image_1 = models.ImageField(upload_to='upload/images', null=True, blank=True, verbose_name='Şəkil Yerləşdir')
    service_support = models.CharField(max_length=255, verbose_name='Service Support:', help_text='Ümumi dəyər 255 olmalıdır!')
    date = models.CharField(max_length=255, verbose_name='Joining Date:', help_text='Ümumi dəyər 255 olmalıdır!')
    years = models.CharField(max_length=255, verbose_name='Years of experience:', help_text='Ümumi dəyər 255 olmalıdır!')
    instagram = models.URLField(max_length=255, null=True, blank=True, verbose_name='Instagram URL')
    facebook = models.URLField(max_length=255, null=True, blank=True, verbose_name='Facebook URL')
    twitter = models.URLField(max_length=255, null=True, blank=True, verbose_name='Twitter URL')
    youtube = models.URLField(max_length=255, null=True, blank=True, verbose_name='YouTube URL')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.name