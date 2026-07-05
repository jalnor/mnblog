from sqlite3.dbapi2 import Date

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    date = models.DateField()
    body = models.TextField()