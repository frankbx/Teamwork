from django.db import models


class Equipment(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
