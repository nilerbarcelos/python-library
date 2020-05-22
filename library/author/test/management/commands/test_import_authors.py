import os
from io import StringIO
from django.core.management import call_command
from django.test import TransactionTestCase

from library.author.models import Author

PATH_FILE = os.path.dirname(os.path.abspath(__file__))


class ImportAuthorsTests(TransactionTestCase):
    def test_command_output_all_authors_created(self):
        out = StringIO()
        try:
            call_command(
                "import_authors",
                os.path.join(PATH_FILE, "test_authors.csv"),
                stdout=out
            )
            expected = """Niler Barcelos created\nJoao Saldanha created\n"""

            authors = Author.objects.all()

            self.assertEqual(expected, out.getvalue())
            self.assertEqual(2, len(authors))
            self.assertEqual("Niler Barcelos", authors[0].name)
            self.assertEqual("Joao Saldanha", authors[1].name)

        finally:
            out.close()

    def test_command_output_authors_already_created(self):
        author_model = Author(name="Niler Barcelos")
        author_model.save()
        out = StringIO()

        try:
            call_command(
                "import_authors",
                os.path.join(PATH_FILE, "test_authors.csv"),
                stdout=out
            )

            expected = """Niler Barcelos already created\nJoao Saldanha created\n"""

            authors = Author.objects.all()

            self.assertEqual(expected, out.getvalue())
            self.assertEqual(2, len(authors))
            self.assertEqual("Niler Barcelos", authors[0].name)
            self.assertEqual("Joao Saldanha", authors[1].name)
        finally:
            out.close()
