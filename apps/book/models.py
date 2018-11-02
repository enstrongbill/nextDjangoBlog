from django.db import models

# Create your models here.
class BookMessage(models.Model):
    title = models.CharField(max_length=20, verbose_name='')