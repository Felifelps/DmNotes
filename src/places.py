from models import Place
from model_view import ModelView


class PlacesView(ModelView):
    model = Place
    model_help_text = "Local"
    title = "Locais"
    