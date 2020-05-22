from django.test import TestCase

from library.author.models import Author
from library.utils.import_data import ImportData


class ImportDataTests(TestCase):
    def test_import_message_author_created(self):
        data = [
            {"name": "Niler Barcelos"},
            {"name": "Joao Saldanha"},
        ]

        import_data = ImportData(Author, data)
        import_data.execute()

        messages = import_data.get_messages()
        authors = [message for message in messages]
        self.assertEqual("Niler Barcelos created", authors[0])
        self.assertEqual("Joao Saldanha created", authors[1])
