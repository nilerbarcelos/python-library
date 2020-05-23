import ujson as json

from django.http import HttpResponse


class BookPresenterDjango(object):
    def __init__(self):
        self._content = {}

    def present_book(self, book):
        self._content = {
            'book_id': book.book_id,
            'name': book.name,
            'edition': book.edition,
            'publication_year': book.publication_year,
            'authors': book.authors
        }

    def create_response(self):
        return HttpResponse(json.dumps(self._content), content_type='application/json')
