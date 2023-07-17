from django.db import models
from fancyusdigital.utils.base import BaseModel
from django.utils.html import format_html
# Create your models here.


class FaqPost(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Question:', help_text='Ümumi dəyər 255 olmalıdır!')
    description = models.TextField(verbose_name='The answer:')

    class Meta:
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.title


class FaqFormEntry(models.Model):
    FirstName = models.CharField(max_length=255)
    EmailAddress = models.EmailField()
    PhoneNo = models.CharField(max_length=255)
    Message = models.TextField()

    class Meta:
        verbose_name = 'Faq form'
        verbose_name_plural = 'Faq form'
        
    def __str__(self):
        return self.FirstName