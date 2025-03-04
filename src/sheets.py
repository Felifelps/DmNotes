from models import Sheet
from model_view import ModelView


class SheetsView(ModelView):
    model = Sheet
    model_help_text = "Ficha"
    title = "Fichas"
    image_field = "image_path"
