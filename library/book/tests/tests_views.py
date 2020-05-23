import ujson
from django.test import TestCase, Client
import http.client

from library.author.models import Author
from library.book.factories.book_gateway_django_factory import BookGatewayDjangoFactory


class BookViewTest(TestCase):
    def setUp(self):
        self.book_gateway_django = BookGatewayDjangoFactory.make()

    def _create_author(self, name=None):
        return Author.objects.create(name=name)

    def test_create_book(self):
        author = self._create_author("Luciano Ramalho")
        request = {
            "name": "Fluent Python",
            "edition": "3",
            "publication_year": 2015,
            "authors": [
                author.author_id
            ]
        }

        response = Client().post("/library/books/", request, content_type="application/json")

        self.assertEqual(http.client.OK, response.status_code)

    def test_update_books(self):
        author = self._create_author("Luciano Ramalho")
        book = self.book_gateway_django.create_book(
            name="Fluent Python",
            edition="3",
            publication_year=2015,
            authors=[author.author_id]
        )
        new_author = self._create_author("Machado de Assis")
        request = {
            "name": "Dom Casmurro",
            "edition": "6",
            "publication_year": 1920,
            "authors": [
                new_author.author_id
            ]
        }

        response = Client().put("/library/books/{id_book}/"
                                .format(id_book=book.book_id),
                                request,
                                content_type="application/json")

        self.assertEqual(http.client.OK, response.status_code)

    def test_get_books(self):
        author = self._create_author("Luciano Ramalho")
        self.book_gateway_django.create_book(
            name="Fluent Python",
            edition="3",
            publication_year=2015,
            authors=[author.author_id]
        )

        response = Client().get("/library/books/")

        self.assertEqual(http.client.OK, response.status_code)

    def test_delete_book(self):
        author = self._create_author("Luciano Ramalho")
        book = self.book_gateway_django.create_book(
            name="Fluent Python",
            edition="3",
            publication_year=2015,
            authors=[author.author_id]
        )

        response = Client().delete("/library/books/{id_book}/".format(id_book=book.book_id))

        self.assertEqual(http.client.OK, response.status_code)
