from django.core.management.base import BaseCommand

from library.author.models import Author
from library.utils.file_read import FileRead
from library.utils.import_data import ImportData


class Command(BaseCommand):
    help = "Create Authors"

    def __init__(self, stdout=None, stderr=None):
        super().__init__(stdout=stdout, stderr=stderr)
        self.data = []
        self.messages = []

    def add_arguments(self, parser):
        parser.add_argument(
            "files",
            nargs='+',
            type=str,
            help="CSV file with the authors"
        )

    def handle(self, *args, **options):
        self._files = options["files"]
        if not self._files:
            return

        for file_import in self._files:
            self._file_read(file_import)
            self._import_authors()
            self._show_messages()

    def _file_read(self, file_import):
        file = FileRead(file_import)
        file.execute()
        self.data = file.get_data()

    def _import_authors(self):
        import_authors = ImportData(Author, self.data)
        import_authors.execute()
        self.messages = import_authors.get_messages()

    def _show_messages(self):
        for message in self.messages:
            self.stdout.write(message)
