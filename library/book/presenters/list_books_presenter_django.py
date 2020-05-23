import ujson as json

from django.http import HttpResponse


class ListBooksPresenterDjango(object):
    def __init__(self):
        self._content = {}

    def present_books(self, books, total_table_records):
        self._content = {
            'books': self._mount_books(books),
            'total_table_records': total_table_records,
        }

    def create_response(self):
        return HttpResponse(json.dumps(self._content), content_type='application/json')

    @classmethod
    def _mount_books(cls, books):
        for book in books:
            yield {
                'book_id': book.book_id,
                'name': book.name,
                'edition': book.edition,
                'publication_year': book.publication_year,
                'authors': book.authors
            }
