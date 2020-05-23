from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from library.author.views import AuthorView

urlpatterns = [
    url(r'^authors/$', csrf_exempt(AuthorView.as_view()), name='authors'),
]
