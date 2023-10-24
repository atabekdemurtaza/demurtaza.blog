from rest_framework import generics
from rest_framework import mixins
from movies.models import Review
from movies.api.serializers import ReviewSerializer


class ReviewList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request=request, *args, **kwargs)


class ReviewRetrieve(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request=request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
