from struct import Struct


class BookStruct(Struct):
    def __init__(self, book_id=None, name=None, edition=None, publication_year=None, authors=None):
        self.book_id = book_id
        self.name = name
        self.edition = edition
        self.publication_year = publication_year
        self.authors = authors
