import csv
import contextlib


class FileRead:
    def __init__(self, file):
        self.data = []
        self.file = file

    def execute(self):
        self._open_file(self.file)

    def get_data(self):
        return self.data

    def _open_file(self, file_import):
        with open(file_import, newline="") as csvfile:
            self._read_file(csvfile)

    def _read_file(self, csvfile):
        reader = csv.reader(csvfile, delimiter=";", quotechar='"')
        self._list_register(reader)

    def _list_register(self, reader):
        keys = []
        for (key, row) in enumerate(reader):
            if self._first_line(key):
                keys = row
                continue
            self._set_data(keys, row)

    def _first_line(self, key):
        if key == 0:
            return True
        return False

    def _set_data(self, keys, row):
        with contextlib.suppress(IndexError):
            data = zip(keys, row)
            self.data.append(dict(data))
