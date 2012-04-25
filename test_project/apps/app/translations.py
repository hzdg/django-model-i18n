from model_i18n import translator

from app.models import Item


class ItemTranslation(translator.ModelTranslation):
    fields = ('title', 'content')
    db_table = 'item_translation'


translator.register(Item, ItemTranslation)
