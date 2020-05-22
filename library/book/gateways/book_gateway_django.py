from library.book.models import Book
from library.core.book.gateways.book_gateway import BookGateway
from library.core.book.structs import BookStruct


class BookGatewayDjango(BookGateway):
    def create_book(self, name=None, edition=None, publication_year=None, authors=None):
        book = Book()
        book.name = name
        book.edition = edition
        book.publication_year = publication_year
        book.save()

        for author in authors:
            book.authors.add(author)

        return self._mount_book_struct(book)

    @staticmethod
    def _mount_book_struct(book):
        return BookStruct(
            name=book.name,
            edition=book.edition,
            publication_year=book.publication_year
        )
