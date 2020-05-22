class AuthorGatewayDjangoFactory(object):
    @staticmethod
    def make():
        from library.author.gateways.author_gateway_django import AuthorGatewayDjango

        return AuthorGatewayDjango()
