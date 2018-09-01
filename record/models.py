from django.db import models

from book.models import Book
from system_auth.models import Workspace, Profile


class Record(models.Model):

    status = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    ref_owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    ref_book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    ref_workspace = models.ForeignKey(Workspace, on_delete=models.DO_NOTHING, blank = True,null=True)

    def __str__(self):
        return self.ref_book.title +" "+self.status
