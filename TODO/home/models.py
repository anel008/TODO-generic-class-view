from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.TextField()
    body = models.TextField()
    def __str__(self):
        return self.title