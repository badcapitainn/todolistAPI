from django.db import models

class Todolist(models.Model):
    name = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)