from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

class ServicePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'description2', 'get_image','title_1','description_3','title_2','description_4','title_3','description_5')
    search_fields = ('title',)
    list_filter = ['title']

    def get_image(self, obj):
        if obj.image2:
            img = '<img src="{url}" width="100px" />'.format(url=obj.image2.url)
            return format_html(img)
        return format_html('<b style="color:green"> No img </b>')

admin.site.register(ServicePost, ServicePostAdmin)