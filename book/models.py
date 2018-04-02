from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):    
    def __init__(self): 
        self.tasks = []
    
    def is_empty(self):
        return len(self.tasks) == 0
    
    def add_task(self, task):
        self.tasks.append(task)
        
    def first_task(self):
        return self.tasks[0]