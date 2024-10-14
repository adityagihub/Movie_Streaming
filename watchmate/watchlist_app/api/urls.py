from django.urls import path
from watchlist_app.api.views import (
    StreamPlatformAV,
    StreamPlatformDetailAV,
    WatchListAv,
    WatchDetailAV,ReviewList,ReviewDetails
)

urlpatterns = [
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('list/', WatchListAv.as_view(), name='watchlist-list'),
    path('list/<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),  # Ensure this name matches the view_name in the serializer
    path('review',ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetails.as_view(),name= 'review-detail'), # Ensure this name matches the view_name in the serial
    
    path('stream/<int:pk>/review',StreamPlatformAV.as_view(), name='stream-details'),
    path('stream/review/<int:pk>',ReviewDetails.as_view(), name='review-details'),
]
