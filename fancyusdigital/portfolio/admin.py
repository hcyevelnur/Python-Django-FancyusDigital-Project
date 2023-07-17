from django.contrib import admin
from .models import *

# Register your models here.

class PortifolioAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'get_image', 'title', 'portifolio_name','description','client_name','date','website','category','title_1','description_3')
    search_fields = ('title',)
    list_filter = ['portifolio_name']

    def get_image(self, obj):
        if obj.image_22:
            img = '<img src="{url}" width="100px" />'.format(url=obj.image_22.url)
            return format_html(img)
        return format_html('<b style="color:green"> No img </b>')

admin.site.register(Portifolio, PortifolioAdmin)


class PortifolioTagAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
    list_filter = ['category']

admin.site.register(PortifolioTag, PortifolioTagAdmin)