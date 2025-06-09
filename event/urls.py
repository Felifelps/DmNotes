# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('new/', views.EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('<int:pk>/edit/', views.EventUpdateView.as_view(), name='event_update'),
    path('<int:pk>/delete/', views.EventDeleteView.as_view(), name='event_delete'),
    path('<int:pk>/toggle_fixed/', views.EventToggleFixedView.as_view(), name='event_toggle_fixed'),
]
