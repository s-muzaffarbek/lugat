from django.db import models


class Lugat(models.Model):
    inglizcha = models.CharField(max_length=99)
    uzbekcha = models.CharField(max_length=99)

