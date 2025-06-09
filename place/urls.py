# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlaceListView.as_view(), name='place_list'),
    path('new/', views.PlaceCreateView.as_view(), name='place_create'),
    path('<int:pk>/', views.PlaceDetailView.as_view(), name='place_detail'),
    path('<int:pk>/edit/', views.PlaceUpdateView.as_view(), name='place_update'),
    path('<int:pk>/delete/', views.PlaceDeleteView.as_view(), name='place_delete'),
    path('<int:pk>/toggle_fixed/', views.PlaceToggleFixedView.as_view(), name='place_toggle_fixed'),
]
