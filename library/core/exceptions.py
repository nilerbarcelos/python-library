class BookDoesNotExistException(Exception):
    def __init__(self, book_id=None):
        message = 'Book id {0} does not exist'.format(book_id)
        super(BookDoesNotExistException, self).__init__(message)
