from django.db import models

class Movie(models.Model):
      title=models.CharField(max_length=20)
      author=models.CharField(max_length=20)
      price=models.IntegerField()

