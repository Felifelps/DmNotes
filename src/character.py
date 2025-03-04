from models import Character
from model_view import ModelView


class CharactersView(ModelView):
    model = Character
    model_help_text = "Personagem"
    title = "Personagens"
    image_field = "image_path"
