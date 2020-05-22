from django.views.generic import View

from library.author.factories.author_gateway_django_factory import AuthorGatewayDjangoFactory
from library.author.presenters.list_authors_presenter_django import ListAuthorsPresenterDjango


class AuthorView(View):
    def get(self, request):
        author_gateway = AuthorGatewayDjangoFactory.make()
        page = int(request.GET.get('page', 1))
        name = request.GET.get('name', None)
        authors, total_table_records = author_gateway.get_authors(name=name, page=page)

        presenter = ListAuthorsPresenterDjango()
        presenter.present_authors(authors, total_table_records)

        return presenter.create_response()
