from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book


class BookViewSetTestCase(APITestCase):
    def setUp(self):
        self.book_data = {
            "title": "Sample Title",
            "author": "Sample Author",
            "published_date": "2024-10-26",
            "isbn": "123456789012",
            "pages": 300,
            "cover": "https://example.com/default-cover.jpg",
            "language": "EN",
        }
        self.book = Book.objects.create(**self.book_data)
        self.url_list = reverse("api:book-list")

    @staticmethod
    def url_detail(pk: int) -> str:
        return reverse("api:book-detail", args=[pk])

    def test_create_book(self):
        book_data = self.book_data.copy()
        book_data["isbn"] = "000000000"
        response = self.client.post(self.url_list, data=book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_list_books(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), Book.objects.count())

    def test_retrieve_book(self):
        response = self.client.get(self.url_detail(self.book.id))
        print(f"{self.url_list}{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_update_book(self):
        updated_data = self.book_data.copy()
        updated_data["title"] = "Updated Book Title"
        response = self.client.put(self.url_detail(self.book.id), data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book Title")

    def test_partial_update_book(self):
        response = self.client.patch(
            self.url_detail(self.book.id), data={"title": "Partially Updated Title"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Partially Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.url_detail(self.book.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
