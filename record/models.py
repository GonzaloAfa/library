from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


from book.models import Book
from system_auth.models import Workspace, Profile

class StatusRecord(models.Model):
    name = models.CharField(max_length=30)

class Record(models.Model):

    active = models.BooleanField(default=True)
    status = models.ForeignKey(StatusRecord, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    ref_owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, blank = True,null=True)
    ref_book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    ref_workspace = models.ForeignKey(Workspace, on_delete=models.DO_NOTHING, blank = True,null=True)

    def __str__(self):
        return self.ref_book.title +" "+self.status


class HistoryRecord(models.Model):

    status = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    ref_owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, blank = True,null=True)
    ref_book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    ref_workspace = models.ForeignKey(Workspace, on_delete=models.DO_NOTHING, blank = True,null=True)
    workspace = models.CharField(max_length=120)

    def __str__(self):
        return self.ref_book.title +" "+self.status


@receiver(post_save, sender=Record)
def add_history_record(sender, instance, created, **kwargs):


    history_record = HistoryRecord(
        status = instance.status,
        ref_owner = instance.ref_owner,
        ref_book = instance.ref_book,
        ref_workspace = instance.ref_workspace
    )

    history_record.save()
