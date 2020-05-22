from django.urls import path

from library.author.views import AuthorView

urlpatterns = [
    path('authors', AuthorView.as_view(), name='authors'),
]