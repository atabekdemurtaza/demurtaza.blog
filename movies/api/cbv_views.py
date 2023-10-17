from rest_framework.views import APIView
from movies.models import Movie
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class WatchListAPIView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAPIView(APIView):

    def get(self, request, lookup):
        if lookup.isdigit():
            movie = get_object_or_404(klass=Movie, id=lookup)
        else:
            movie = get_object_or_404(klass=Movie, name=lookup)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, lookup):
        if lookup.isdigit():
            movie = get_object_or_404(klass=Movie, id=lookup)
        else:
            movie = get_object_or_404(klass=Movie, name=lookup)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, lookup):
        if lookup.isdigit():
            movie = get_object_or_404(klass=Movie, id=lookup)
        else:
            movie = get_object_or_404(klass=Movie, name=lookup)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
