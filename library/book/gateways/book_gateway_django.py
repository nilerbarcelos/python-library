from django.db.models import Q

from library.book.models import Book
from library.core.book.gateways.book_gateway import BookGateway, RECORDS_IN_PAGINATION
from library.core.book.structs import BookStruct
from future.utils import lmap

from library.core.exceptions import BookDoesNotExistException


class BookGatewayDjango(BookGateway):
    def create_book(self, name=None, edition=None, publication_year=None, authors=None):
        book = Book()
        book.name = name
        book.edition = edition
        book.publication_year = publication_year
        book.save()

        for author in authors:
            book.authors.add(author)

        return self.get_book_by_id(book_id=book.book_id)

    def filter_default(self):
        return Q()

    def get_books(self, name=None, edition=None, publication_year=None,
                  author=None, page=None, records_in_pagination=RECORDS_IN_PAGINATION):
        offset = None
        limit = None

        if page and records_in_pagination:
            offset = (page * records_in_pagination) - records_in_pagination
            limit = offset + records_in_pagination

        parameter = self.filter_default()
        if name is not None:
            parameter &= Q(name=name)
        if edition is not None:
            parameter &= Q(edition=edition)
        if publication_year is not None:
            parameter &= Q(publication_year=publication_year)
        if author is not None:
            parameter &= Q(authors__name=author)

        registers = Book.objects.prefetch_related('authors').filter(parameter)[offset:limit]
        total_table_records = Book.objects.filter(parameter).count()
        books = lmap(self._mount_book_struct, registers)

        return books, total_table_records

    def get_book_by_id(self, book_id):
        try:
            book = Book.objects.prefetch_related('authors').get(id=book_id)
        except Book.DoesNotExist:
            raise BookDoesNotExistException(book_id)

        return self._mount_book_struct(book)

    def delete_book(self, book_id):
        Book.objects.filter(id=book_id).delete()

    @staticmethod
    def _mount_book_struct(book):
        return BookStruct(
            book_id=book.book_id,
            name=book.name,
            edition=int(book.edition),
            publication_year=book.publication_year,
            authors=[author.name for author in book.authors.all()]
        )
