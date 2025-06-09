# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CampaignListView.as_view(), name='campaign_list'),
    path('campaign/<int:campaign_pk>/', views.CampaignDetailView.as_view(), name='campaign_detail'),
    path('campaign/new/', views.CampaignCreateView.as_view(), name='campaign_create'),
    path('campaign/<int:campaign_pk>/edit/', views.CampaignUpdateView.as_view(), name='campaign_update'),
    path('campaign/<int:campaign_pk>/delete/', views.CampaignDeleteView.as_view(), name='campaign_delete'),

    path('campaign/<int:campaign_pk>/characters/', include('character.urls')),
    path('campaign/<int:campaign_pk>/dungeons/', include('dungeon.urls')),
    path('campaign/<int:campaign_pk>/events/', include('event.urls')),
    path('campaign/<int:campaign_pk>/items/', include('item.urls')),
    path('campaign/<int:campaign_pk>/places/', include('place.urls')),
    path('campaign/<int:campaign_pk>/sheets/', include('sheet.urls')),
]
