# filters.py
from django_filters import rest_framework as filters

from .models import Book


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(lookup_expr="icontains")
    language = filters.CharFilter(lookup_expr="exact")
    published_year = filters.NumberFilter(field_name="published_date", lookup_expr="year")


    class Meta:
        model = Book
        fields = ["author", "language", "published_date"]
