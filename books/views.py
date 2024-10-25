from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from . import models
from .serializers import BookSerializer


class BookAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 2


class BookAPIList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookAPIListPagination


class BookAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = (TokenAuthentication, )


class BookAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer
