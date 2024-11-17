from django.urls import path
from imdb_api import views   # Import views from your app

urlpatterns = [
    # Example URL pattern
    path('list/', views.movie_list, name='movie-list'),
    path('list/<int:pk>', views.movie_detail, name='movie-detail'),

    path('stream/', views.StreamPlatformList.as_view(), name='stream-platform'),
    path('stream/<int:pk>', views.StreamPlatformDetail.as_view(), name='stream-platform-detail'),
    path('', views.api_root, name='api-root'),
]
