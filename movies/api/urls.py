from django.urls import path
# from .fbv_views import movie_list, movie_detail
from .cbv_views import MovieList, MovieDetail


"""# Function-based-views
urlpatterns = [
    path(route='list/', view=movie_list, name='movie-list'),
    path(route='list/<lookup>/', view=movie_detail, name='movie-detail')
]"""

# Class-based-views
urlpatterns = [
    path(
        route='list/',
        view=MovieList.as_view(),
        name='movie-list'),
    path(
        route='list/<lookup>/',
        view=MovieDetail.as_view(),
        name='movie-detail')
]
