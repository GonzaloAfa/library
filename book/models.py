from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     self.name = self.name.capitalize().strip()
    #     super(Author, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120)

    description = models.TextField()
    previewLink = models.TextField()
    imagen = models.TextField()

    ref_author = models.ManyToManyField(Author)
    ref_category = models.ManyToManyField(Category)
    ISBN = models.CharField(max_length=13, primary_key=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.ISBN = self.ISBN.replace("-","").strip()
        super(Book, self).save(*args, **kwargs)
