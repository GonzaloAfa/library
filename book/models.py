from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=60)
    authors = models.ManyToManyField(Author)
    ref_author = models.CharField(max_length=30)
    ref_category = models.CharField(max_length=30)
    ISBN = models.CharField(max_length=13, primary_key=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.ISBN = self.ISBN.replace("-","").strip()
        super(Book, self).save(*args, **kwargs)
