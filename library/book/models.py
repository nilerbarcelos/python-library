from django.db import models

from library.author.models import Author


class Book(models.Model):
    name = models.CharField(max_length=255)
    edition = models.CharField(max_length=10)
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    @property
    def book_id(self):
        return self.id
