from rest_framework import generics
from movies.models import Review
from movies.api.serializers import ReviewSerializer


class ReviewList(generics.ListAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)

    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return Review.objects.filter(watchlist=pk)


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

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
