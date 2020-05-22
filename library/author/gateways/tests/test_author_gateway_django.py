from django.test import TestCase

from library.author.factories.author_gateway_django_factory import AuthorGatewayDjangoFactory
from library.author.models import Author


class AuthorGatewayDjangoTestCase(TestCase):
    def setUp(self):
        self.author_gateway_django = AuthorGatewayDjangoFactory.make()

    def _create_author(self, name=None):
        return Author.objects.create(name=name or 'Machado de Assis')


class GetAuthorsTests(AuthorGatewayDjangoTestCase):
    def test_get_authors(self):
        expected_author = self._create_author()

        authors, _ = self.author_gateway_django.get_authors(page=1)

        self.assertEqual(1, len(authors))
        self.assertEqual(expected_author.author_id, authors[0].author_id)
        self.assertEqual(expected_author.name, authors[0].name)

    def test_get_authors_by_name(self):
        expected_author = self._create_author(name='Machado de Assis')
        self._create_author(name='Graciliano Ramos')

        authors, _ = self.author_gateway_django.get_authors(name='Machado de Assis')

        self.assertEqual(1, len(authors))
        self.assertEqual(expected_author.author_id, authors[0].author_id)
        self.assertEqual(expected_author.name, authors[0].name)

    def test_limits_the_number_of_records(self):
        self._create_author(name='Machado de Assis')
        self._create_author(name='Graciliano Ramos')

        authors, total_table_records = self.author_gateway_django.get_authors(
            page=1,
            records_in_pagination=1
        )

        self.assertEqual(1, len(authors))
        self.assertEqual(2, total_table_records)

    def test_pagination(self):
        self._create_author(name='Machado de Assis')
        author_of_page_two = self._create_author(name='Graciliano Ramos')

        authors, total_table_records = self.author_gateway_django.get_authors(
            page=2,
            records_in_pagination=1
        )

        self.assertEqual(1, len(authors))
        self.assertEqual(author_of_page_two.author_id, authors[0].author_id)
        self.assertEqual(author_of_page_two.name, authors[0].name)
