from rest_framework.views import APIView
from movies.models import MovieList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatFormSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class WatchListAPIView(APIView):

    def get(self, request):
        movies = MovieList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAPIView(APIView):

    def get(self, request, lookup):
        if lookup.isdigit():
            movie = get_object_or_404(klass=MovieList, id=lookup)
        else:
            movie = get_object_or_404(klass=MovieList, title=lookup)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, lookup):
        if lookup.isdigit():
            movie = get_object_or_404(klass=MovieList, id=lookup)
        else:
            movie = get_object_or_404(klass=MovieList, title=lookup)

        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, lookup):
        if lookup.isdigit():
            movie = get_object_or_404(klass=MovieList, id=lookup)
        else:
            movie = get_object_or_404(klass=MovieList, title=lookup)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamListAPIView(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatFormSerializer(
            instance=platform,
            many=True
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = StreamPlatFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
