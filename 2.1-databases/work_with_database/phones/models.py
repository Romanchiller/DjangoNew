from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, default=None, unique=True)
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.BigIntegerField(default=0)
    image = models.FilePathField(max_length=200)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField(default=False)




