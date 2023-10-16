from movies.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(http_method_names=['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def movie_detail(request, lookup):

    if request.method == 'GET':
        if lookup.isdigit():
            movie = get_object_or_404(klass=Movie, id=lookup)
            serializer = MovieSerializer(movie)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        else:
            movie = get_object_or_404(klass=Movie, name=lookup)
            serializer = MovieSerializer(movie)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

    if request.method == 'PUT':
        if lookup.isdigit():
            movie = get_object_or_404(klass=Movie, id=lookup)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data=serializer.data,
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            movie = get_object_or_404(klass=Movie, name=lookup)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data=serializer.data,
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

    if request.method == 'DELETE':
        if lookup.isdigit():
            movie = get_object_or_404(klass=Movie, id=lookup)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            movie = get_object_or_404(klass=Movie, name=lookup)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
