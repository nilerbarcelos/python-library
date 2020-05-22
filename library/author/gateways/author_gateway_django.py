from django.db.models import Q

from library.author.models import Author
from library.core.author.gateways.author_gateway import AuthorGateway, RECORDS_IN_PAGINATION
from library.core.author.structs import AuthorStruct
from future.utils import lmap


class AuthorGatewayDjango(AuthorGateway):
    def filter_default(self):
        return Q()

    def get_authors(self, name=None, page=None, records_in_pagination=RECORDS_IN_PAGINATION):
        offset = None
        limit = None

        if page and records_in_pagination:
            offset = (page * records_in_pagination) - records_in_pagination
            limit = offset + records_in_pagination

        parameter = self.filter_default()
        if name is not None:
            parameter &= Q(name=name)

        registers = Author.objects.filter(parameter)[offset:limit]
        total_table_records = Author.objects.filter(parameter).count()
        authors = lmap(self._mount_author_struct, registers)

        return authors, total_table_records

    def _mount_author_struct(self, author):
        return AuthorStruct(
            author_id=author.author_id,
            name=author.name
        )
