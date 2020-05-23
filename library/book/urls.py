from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from library.book.views import BookView

urlpatterns = [
    url(r'^books/$', csrf_exempt(BookView.as_view()), name='books'),
    url(r'^books/(?P<id_book>\d+)/$', csrf_exempt(BookView.as_view()), name='books'),
]