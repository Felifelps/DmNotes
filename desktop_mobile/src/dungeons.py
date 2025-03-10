from models import Dungeon
from model_view import ModelView


class DungeonsView(ModelView):
    model = Dungeon
    model_help_text = "Masmorra"
    title = "Masmorras"
    image_field = "image_path"
