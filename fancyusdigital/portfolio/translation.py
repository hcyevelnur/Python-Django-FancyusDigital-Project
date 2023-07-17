from modeltranslation.translator import register, TranslationOptions
from .models import Portifolio

@register(Portifolio)
class PortifolioTranslationOptions(TranslationOptions):
    fields = ('title', 'portifolio_name', 'description','client_name','website','title_1','description_3')