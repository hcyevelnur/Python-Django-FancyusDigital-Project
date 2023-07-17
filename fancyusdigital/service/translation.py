from modeltranslation.translator import register, TranslationOptions
from .models import ServicePost

@register(ServicePost)
class ServicePostTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'description2','title_1','description_3','title_2','description_4','title_3','description_5')