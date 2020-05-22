import os
from django.test import TestCase

from library.utils.file_read import FileRead

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class FileReadTests(TestCase):
    def test_file_read(self):
        file_read_csv = os.path.join(BASE_DIR, "test_authors.csv")
        file_read = FileRead(file_read_csv)
        file_read.execute()
        expected = [
            {"name": "Niler Barcelos"},
            {"name": "Joao Saldanha"},
        ]

        data = file_read.get_data()

        self.assertEqual(expected, data)
