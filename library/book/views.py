from django.views.generic import View
from django.http import HttpResponse
import http.client

from library.book.factories.book_gateway_django_factory import BookGatewayDjangoFactory
from library.book.presenters.book_presenter_django import BookPresenterDjango
from library.book.presenters.list_books_presenter_django import ListBooksPresenterDjango

from library.utils.forms.json_form import JsonForm
from past.builtins import basestring
from voluptuous import Schema, Required, All, Length


class BookPostJson(JsonForm):
    schema = Schema({
        Required('name'): basestring,
        Required('edition'): basestring,
        Required('publication_year'): int,
        Required('authors'): All([int], Length(min=1)),
    })


class BookView(View):
    def get(self, request):
        book_gateway = BookGatewayDjangoFactory.make()
        page = int(request.GET.get('page', 1))
        name = request.GET.get('name', None)
        edition = request.GET.get('edition', None)
        publication_year = request.GET.get('publication_year', None)
        author = request.GET.get('author', None)
        books, total_table_records = book_gateway.get_books(
            name=name,
            edition=edition,
            publication_year=publication_year,
            author=author,
            page=page
        )

        presenter = ListBooksPresenterDjango()
        presenter.present_books(books, total_table_records)

        return presenter.create_response()

    def post(self, request):
        form = BookPostJson(request.body)
        if form.is_valid():
            cleaned_value = form.cleaned_value()
            book = BookGatewayDjangoFactory.make().create_book(
                name=cleaned_value.get('name'),
                edition=cleaned_value.get('edition'),
                publication_year=cleaned_value.get('publication_year'),
                authors=cleaned_value.get('authors')
            )

            presenter = BookPresenterDjango()
            presenter.present_book(book)

            return presenter.create_response()

        else:
            return form.create_error_response()

    def put(self, request, id_book):
        form = BookPostJson(request.body)
        if form.is_valid():
            cleaned_value = form.cleaned_value()
            book = BookGatewayDjangoFactory.make().update_book(
                book_id=id_book,
                name=cleaned_value.get('name'),
                edition=cleaned_value.get('edition'),
                publication_year=cleaned_value.get('publication_year'),
                authors=cleaned_value.get('authors')
            )

            presenter = BookPresenterDjango()
            presenter.present_book(book)

            return presenter.create_response()

        else:
            return form.create_error_response()

    def delete(self, request, id_book):
        BookGatewayDjangoFactory.make().delete_book(id_book)

        return HttpResponse(content='', status=http.client.OK, content_type='application/json')

