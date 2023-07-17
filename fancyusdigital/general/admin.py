from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from general.models import *

admin.site.site_header = 'Fancy Us Digital'
admin.site.site_title = 'Project'


class ContactFormEntryAdmin(admin.ModelAdmin):
    list_display = ['FirstName', 'LastName', 'EmailAddress', 'PhoneNo', 'Message']
    list_filter = ['FirstName', 'LastName', 'EmailAddress']
    search_fields = ['FirstName', 'LastName', 'EmailAddress']

class EmailAdressFromAdmin(admin.ModelAdmin):
    list_display = ('EmailAddress',)
    search_fields = ('EmailAddress',)
    list_filter = ['EmailAddress']



class TeslimationPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'description', 'get_image')
    search_fields = ('name',)
    list_filter = ['work']

    def get_image(self, obj):
        if obj.image_1:
            img = '<img src="{url}" width="100px" />'.format(url=obj.image_1.url)
            return format_html(img)
        return format_html('<b style="color:green"> No img </b>')

admin.site.register(TeslimationPost, TeslimationPostAdmin)



admin.site.register(EmailAdressFrom, EmailAdressFromAdmin)
admin.site.register(ContactFormEntry, ContactFormEntryAdmin)



