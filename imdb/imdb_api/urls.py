from django.urls import path ,include
from imdb_api import views   # Import views from your app
from .views import StreamPlatformViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stream', StreamPlatformViewSet, basename='stream')

# streamplatform_list = StreamPlatformViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# streamplatform_detail = StreamPlatformViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
urlpatterns = [
    # Example URL pattern
    path('list/', views.movie_list.as_view(), name='movie-list'),
    path('list/<int:pk>', views.movie_detail.as_view(), name='movie-detail'),

    path('', include(router.urls)),
    # path('stream/', streamplatform_list, name='stream-list'),
    # path('stream/<int:pk>/', streamplatform_detail, name='stream-detail'),
    # path('stream/', views.StreamPlatformList.as_view(), name='stream-platform'),
    # path('stream/<int:pk>', views.StreamPlatformDetail.as_view(), name='streamplatform-detail'),
    path('', views.api_root, name='api-root'),
]
