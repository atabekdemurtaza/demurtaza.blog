from rest_framework import generics
from movies.models import Review, MovieList
from movies.api.serializers import ReviewSerializer
from rest_framework.validators import ValidationError


class ReviewList(generics.ListAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()


class ReviewRetrieve(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request=request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReviewCreate(generics.CreateAPIView):

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = MovieList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(
            watchlist=watchlist,
            review_user=review_user
        )

        if review_queryset.exists():
            raise ValidationError('You have already reviewed this movie!')

        serializer.save(
            watchlist=watchlist,
            review_user=review_user
        )
