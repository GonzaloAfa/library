from django.contrib import admin

# Register your models here.
from .models import Record, HistoryRecord

admin.site.register(Record)
admin.site.register(HistoryRecord)
