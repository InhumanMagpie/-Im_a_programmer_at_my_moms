from django.db import models
from django.contrib import admin

# Create your models here.


class Blog(models.Model):
    header = models.CharField(max_length=100, null=False)
    posts = models.CharField(max_length=500, null=False)
    time = models.DateTimeField(auto_now=True)


admin.site.register(Blog)
