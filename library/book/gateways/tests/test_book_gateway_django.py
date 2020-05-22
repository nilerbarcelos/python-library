from django.test import TestCase

from library.author.models import Author
from library.book.factories.book_gateway_django_factory import BookGatewayDjangoFactory
from library.book.models import Book
from library.core.exceptions import BookDoesNotExistException


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


class GetBooksTests(BookGatewayDjangoTestCase):
    def test_get_books(self):
        expected_author = self._create_author(name="Luciano Ramalho")
        expected_book = self.book_gateway_django.create_book(
            name="Fluent Python",
            edition=2,
            publication_year=2015,
            authors=[expected_author.author_id]
        )

        books, _ = self.book_gateway_django.get_books()

        self.assertEqual(1, len(books))
        self.assertEqual(expected_book.book_id, books[0].book_id)
        self.assertEqual(expected_book.name, books[0].name)
        self.assertEqual([expected_author.name], books[0].authors)

    def test_get_books_by_name(self):
        expected_author = self._create_author(name="Luciano Ramalho")
        expected_book = self.book_gateway_django.create_book(
            name="Fluent Python",
            edition=2,
            publication_year=2015,
            authors=[expected_author.author_id]
        )

        books, _ = self.book_gateway_django.get_books(name="Fluent Python")

        self.assertEqual(1, len(books))
        self.assertEqual(expected_book.book_id, books[0].book_id)
        self.assertEqual(expected_book.name, books[0].name)
        self.assertEqual([expected_author.name], books[0].authors)

    def test_get_books_by_edition(self):
        expected_author = self._create_author(name="Luciano Ramalho")
        expected_book = self.book_gateway_django.create_book(
            name="Fluent Python",
            edition=2,
            publication_year=2015,
            authors=[expected_author.author_id]
        )

        books, _ = self.book_gateway_django.get_books(edition=2)

        self.assertEqual(1, len(books))
        self.assertEqual(expected_book.book_id, books[0].book_id)
        self.assertEqual(expected_book.name, books[0].name)
        self.assertEqual([expected_author.name], books[0].authors)

    def test_get_books_by_publication_year(self):
        expected_author = self._create_author(name="Luciano Ramalho")
        expected_book = self.book_gateway_django.create_book(
            name="Fluent Python",
            edition=2,
            publication_year=2015,
            authors=[expected_author.author_id]
        )

        books, _ = self.book_gateway_django.get_books(publication_year=2015)

        self.assertEqual(1, len(books))
        self.assertEqual(expected_book.book_id, books[0].book_id)
        self.assertEqual(expected_book.name, books[0].name)
        self.assertEqual([expected_author.name], books[0].authors)

    def test_get_books_by_author(self):
        expected_author = self._create_author(name="Luciano Ramalho")
        expected_book = self.book_gateway_django.create_book(
            name="Fluent Python",
            edition=2,
            publication_year=2015,
            authors=[expected_author.author_id]
        )

        books, _ = self.book_gateway_django.get_books(author=expected_author.name)

        self.assertEqual(1, len(books))
        self.assertEqual(expected_book.book_id, books[0].book_id)
        self.assertEqual(expected_book.name, books[0].name)
        self.assertEqual([expected_author.name], books[0].authors)

    def test_limits_the_number_of_records(self):
        author_1 = self._create_author(name="Luciano Ramalho")
        self.book_gateway_django.create_book(
            name="Fluent Python",
            edition=2,
            publication_year=2015,
            authors=[author_1.author_id]
        )
        author_2 = self._create_author(name="Machado de Assis")
        self.book_gateway_django.create_book(
            name="Dom Casmurro",
            edition=4,
            publication_year=1990,
            authors=[author_2.author_id]
        )

        authors, total_table_records = self.book_gateway_django.get_books(
            page=1,
            records_in_pagination=1
        )

        self.assertEqual(1, len(authors))
        self.assertEqual(2, total_table_records)

    def test_pagination(self):
        author_1 = self._create_author(name="Luciano Ramalho")
        self.book_gateway_django.create_book(
            name="Fluent Python",
            edition=2,
            publication_year=2015,
            authors=[author_1.author_id]
        )
        author_of_page_two = self._create_author(name="Machado de Assis")
        book_of_page_two = self.book_gateway_django.create_book(
            name="Dom Casmurro",
            edition=4,
            publication_year=1990,
            authors=[author_of_page_two.author_id]
        )

        books, total_table_records = self.book_gateway_django.get_books(
            page=2,
            records_in_pagination=1
        )

        self.assertEqual(1, len(books))
        self.assertEqual(book_of_page_two.book_id, books[0].book_id)
        self.assertEqual(book_of_page_two.name, books[0].name)


class GetBookByIdTests(BookGatewayDjangoTestCase):
    def test_get_book_by_id(self):
        author = self._create_author(name="Luciano Ramalho")
        book = self.book_gateway_django.create_book(
            name="Fluent Python",
            edition=2,
            publication_year=2015,
            authors=[author.author_id]
        )

        returned_book = self.book_gateway_django.get_book_by_id(book.book_id)

        self.assertEqual(book.book_id, returned_book.book_id)
        self.assertEqual(book.name, returned_book.name)
        self.assertEqual([author.name], returned_book.authors)

    def test_triggers_exception_when_book_does_not_exist(self):
        with self.assertRaises(BookDoesNotExistException):
            self.book_gateway_django.get_book_by_id(9999)


class DeleteBookTests(BookGatewayDjangoTestCase):
    def test_delete_book(self):
        author = self._create_author(name="Luciano Ramalho")
        book = self.book_gateway_django.create_book(
            name="Fluent Python",
            edition=2,
            publication_year=2015,
            authors=[author.author_id]
        )

        self.book_gateway_django.delete_book(book.book_id)

        with self.assertRaises(BookDoesNotExistException):
            self.book_gateway_django.get_book_by_id(book.book_id)
