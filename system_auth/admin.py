from django.contrib import admin

# Register your models here.
from .models import Workspace, Profile

admin.site.register(Workspace)
admin.site.register(Profile)
