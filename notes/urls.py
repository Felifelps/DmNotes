# urls.py
from django.urls import path
from notes import views

urlpatterns = [
    path('new/', views.NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>/update/', views.NoteUpdateView.as_view(), name='note_update'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
    path('<int:pk>/toggle_fixed/', views.NoteToggleFixedView.as_view(), name='note_toggle_fixed'),
]
