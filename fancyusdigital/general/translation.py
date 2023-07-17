from modeltranslation.translator import register, TranslationOptions
from .models import TeslimationPost

@register(TeslimationPost)
class TeslimationPostTranslationOptions(TranslationOptions):
    fields = ('name', 'work', 'description')