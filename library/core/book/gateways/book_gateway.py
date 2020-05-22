RECORDS_IN_PAGINATION = 2


class BookGateway(object):
    def create_book(self, name=None, edition=None, publication_year=None, authors=None):
        raise NotImplementedError

    def get_books(self, name=None, edition=None, publication_year=None, author=None,
                  page=None, records_in_pagination=RECORDS_IN_PAGINATION):
        raise NotImplementedError

    def get_book_by_id(self, book_id):
        raise NotImplementedError

    def delete_book(self, book_id):
        raise NotImplementedError
