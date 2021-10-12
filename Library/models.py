from django.db import models


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=24, default='author name')
    publisher = models.CharField(max_length=24, default='publisher name')
    published_at = models.DateTimeField(auto_now=True)
    cover = models.TextField(default='simple book cover')

    def __str__(self):
        return self.author
