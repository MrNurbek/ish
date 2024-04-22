from page.models import User

from modeltranslation.translator import translator, TranslationOptions


class ModelkaTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Modelka.
    """

    fields = ('name', 'description',)


translator.register(User, ModelkaTranslationOptions)