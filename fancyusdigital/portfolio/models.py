from django.db import models
from fancyusdigital.utils.base import BaseModel
from django.utils.html import format_html

# Create your models here.

class PortifolioTag(BaseModel):
    category = models.CharField(max_length=25, verbose_name='Tag: ')

    class Meta:
        verbose_name = 'Portifolio Tag'
        verbose_name_plural = 'Portifolio Tag'

    def __str__(self):
        return self.category

class Portifolio(BaseModel):
    image_1 = models.ImageField(upload_to='upload/images', null=True, blank=True, verbose_name='Şəkil Yerləşdir')
    image_22 = models.ImageField(upload_to='upload/images', null=True, blank=True, verbose_name='Mobil Telefon üçün şəkil yerləşdir')
    title = models.CharField(max_length=255, verbose_name='Başlıq:', help_text='Ümumi dəyər 255 olmalıdır!', null=True, blank=True,)
    portifolio_name = models.CharField(max_length=255, verbose_name='Portfolio adı:', help_text='Ümumi dəyər 255 olmalıdır!', null=True, blank=True,)
    description = models.TextField(verbose_name='Haqqında:', null=True, blank=True,)
    client_name = models.CharField(max_length=255, verbose_name='Client Name:', help_text='Ümumi dəyər 255 olmalıdır!', null=True, blank=True,)
    date = models.DateField(verbose_name='Post Date', null=True, blank=True,)
    website = models.CharField(max_length=255, verbose_name='Website:', help_text='Ümumi dəyər 255 olmalıdır!', null=True, blank=True,)
    category = models.ForeignKey('portfolio.PortifolioTag', on_delete=models.CASCADE, related_name='portifolio_tag', verbose_name='Category:', null=True, blank=True,)
    title_1 = models.CharField(max_length=255, verbose_name='Başlıq:', help_text='Ümumi dəyər 255 olmalıdır!', null=True, blank=True,)
    description_3 = models.TextField(verbose_name='Haqqında:', null=True, blank=True,)
    
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Normal Portfolio'

    def __str__(self):
        return self.portifolio_name