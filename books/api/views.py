from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from books.filters import BookFilter
from books.models import Book

from .serializers import BookSerializer


class BooksViewSet(
    RetrieveModelMixin,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
