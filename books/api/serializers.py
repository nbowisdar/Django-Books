from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from books.models import Book


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Example Book",
            value={
                "title": "Sample Title",
                "author": "Sample Author",
                "published_date": "2024-10-26",
                "isbn": "1234567890123",
                "pages": 300,
                "cover": "https://example.com/default-cover.jpg",
                "language": "EN",
            },
            description="An example of the Book object with default values.",
        ),
    ]
)
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
