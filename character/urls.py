# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
    path('new/', views.CharacterCreateView.as_view(), name='character_create'),
    path('<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
    path('<int:pk>/edit/', views.CharacterUpdateView.as_view(), name='character_update'),
    path('<int:pk>/delete/', views.CharacterDeleteView.as_view(), name='character_delete'),
    path('<int:pk>/toggle_fixed/', views.CharacterToggleFixedView.as_view(), name='character_toggle_fixed'),
]
