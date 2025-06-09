# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SheetListView.as_view(), name='sheet_list'),
    path('new/', views.SheetCreateView.as_view(), name='sheet_create'),
    path('<int:pk>/', views.SheetDetailView.as_view(), name='sheet_detail'),
    path('<int:pk>/edit/', views.SheetUpdateView.as_view(), name='sheet_update'),
    path('<int:pk>/delete/', views.SheetDeleteView.as_view(), name='sheet_delete'),
    path('<int:pk>/toggle_fixed/', views.SheetToggleFixedView.as_view(), name='sheet_toggle_fixed'),
]
