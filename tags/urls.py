# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TagListView.as_view(), name='tag_list'),
    path('new/', views.TagCreateView.as_view(), name='tag_create'),
    path('<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
]
