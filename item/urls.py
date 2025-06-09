# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    path('new/', views.ItemCreateView.as_view(), name='item_create'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_update'),
    path('<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
    path('<int:pk>/toggle_fixed/', views.ItemToggleFixedView.as_view(), name='item_toggle_fixed'),
]
