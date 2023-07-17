from modeltranslation.translator import register, TranslationOptions
from .models import TeamPost

@register(TeamPost)
class TeamPostTranslationOptions(TranslationOptions):
    fields = ('name', 'work', 'description','service_support')