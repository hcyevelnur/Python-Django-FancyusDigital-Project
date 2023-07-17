from modeltranslation.translator import register, TranslationOptions
from .models import FaqPost

@register(FaqPost)
class FaqPostTranslationOptions(TranslationOptions):
    fields = ('title', 'description')