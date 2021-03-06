RECORDS_IN_PAGINATION = 5


class AuthorGateway(object):
    def get_authors(self, name=None, page=None, records_in_pagination=RECORDS_IN_PAGINATION):
        raise NotImplementedError
