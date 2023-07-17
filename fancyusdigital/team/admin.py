from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

class TeamPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'description', 'get_image','service_support','date','years','instagram','facebook','twitter','youtube')
    search_fields = ('name',)
    list_filter = ['work']

    def get_image(self, obj):
        if obj.image_1:
            img = '<img src="{url}" width="100px" />'.format(url=obj.image_1.url)
            return format_html(img)
        return format_html('<b style="color:green"> No img </b>')

admin.site.register(TeamPost, TeamPostAdmin)