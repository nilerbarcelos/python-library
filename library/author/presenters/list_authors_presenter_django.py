import ujson as json

from django.http import HttpResponse


class ListAuthorsPresenterDjango(object):
    def __init__(self):
        self._content = {}

    def present_authors(self, authors, total_table_records):
        self._content = {
            'authors': self._mount_authors(authors),
            'total_table_records': total_table_records,
        }

    def create_response(self):
        return HttpResponse(json.dumps(self._content), content_type='application/json')

    @classmethod
    def _mount_authors(cls, authors):
        for author in authors:
            yield {
                'author_id': author.author_id,
                'name': author.name
            }
