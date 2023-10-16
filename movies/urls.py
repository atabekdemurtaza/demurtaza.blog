from django.urls import path
from .views import movie_list, movie_detail

urlpatterns = [
    path(route='list/', view=movie_list, name='movie-list'),
    path(route='<int:pk>/', view=movie_detail, name='movie-detail')
]
