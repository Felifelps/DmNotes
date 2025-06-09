# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DungeonListView.as_view(), name='dungeon_list'),
    path('new/', views.DungeonCreateView.as_view(), name='dungeon_create'),
    path('<int:pk>/', views.DungeonDetailView.as_view(), name='dungeon_detail'),
    path('<int:pk>/edit/', views.DungeonUpdateView.as_view(), name='dungeon_update'),
    path('<int:pk>/delete/', views.DungeonDeleteView.as_view(), name='dungeon_delete'),
    path('<int:pk>/toggle_fixed/', views.DungeonToggleFixedView.as_view(), name='dungeon_toggle_fixed'),
]
