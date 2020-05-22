from struct import Struct


class AuthorStruct(Struct):
    def __init__(self, author_id=None, name=None):
        self.author_id = author_id
        self.name = name
