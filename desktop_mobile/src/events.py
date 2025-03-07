from models import Event
from model_view import ModelView


class EventsView(ModelView):
    model = Event
    model_help_text = "Evento"
    title = 'Eventos'
    