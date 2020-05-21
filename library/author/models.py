from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    @property
    def author_id(self):
        return self.id