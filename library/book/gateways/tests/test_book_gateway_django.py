from django.test import TestCase

from library.author.models import Author
from library.book.factories.book_gateway_django_factory import BookGatewayDjangoFactory
from library.book.models import Book


class BookGatewayDjangoTestCase(TestCase):
    def setUp(self):
        self.book_gateway_django = BookGatewayDjangoFactory.make()

    def _create_author(self, name=None):
        return Author.objects.create(name=name)

    def _create_book(self, name=None, edition=None, publication_year=None, authors=None):
        return Book.objects.create(
            name=name,
            edition=edition,
            publication_year=publication_year,
            authors=authors
        )


class CreateBookTests(BookGatewayDjangoTestCase):
    def test_create_book(self):
        author = self._create_author(name="Luciano Ramalho")
        name = "Fluent Python"
        edition = 2
        publication_year = 2015
        authors = [author.author_id]

        book = self.book_gateway_django.create_book(
            name=name,
            edition=edition,
            publication_year=publication_year,
            authors=authors
        )

        self.assertEqual(name, book.name)
        self.assertEqual(edition, book.edition)
        self.assertEqual(publication_year, book.publication_year)
