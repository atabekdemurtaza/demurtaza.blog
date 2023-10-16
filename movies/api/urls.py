from django.urls import path
from .fbv_views import movie_list, movie_detail

urlpatterns = [
    path(route='list/', view=movie_list, name='movie-list'),
    path(route='list/<lookup>/', view=movie_detail, name='movie-detail')
]
