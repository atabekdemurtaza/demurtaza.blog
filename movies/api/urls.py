from django.urls import path
# from .fbv_views import movie_list, movie_detail
from .cbv_views import WatchDetailAPIView, WatchListAPIView
from .cbv_views import StreamListAPIView


"""# Function-based-views
urlpatterns = [
    path(route='list/', view=movie_list, name='movie-list'),
    path(route='list/<lookup>/', view=movie_detail, name='movie-detail')
]"""

# Class-based-views
urlpatterns = [
    path(
        route='list/',
        view=WatchListAPIView.as_view(),
        name='movie-list'),
    path(
        route='list/<lookup>/',
        view=WatchDetailAPIView.as_view(),
        name='movie-detail'),
    path(
        route='stream/',
        view=StreamListAPIView.as_view(),
        name='stream-list',
    )
]
