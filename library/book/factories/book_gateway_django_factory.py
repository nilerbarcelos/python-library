class BookGatewayDjangoFactory(object):
    @staticmethod
    def make():
        from library.book.gateways.book_gateway_django import BookGatewayDjango

        return BookGatewayDjango()
