from models import Item
from model_view import ModelView


class ItemsView(ModelView):
    model = Item
    model_help_text = "Item"
    title = "Itens"
    