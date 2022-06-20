from django.db import models
from django.contrib import admin

# Create your models here.


class BaseContent(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class TextPost(BaseContent):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    image_content = models.ImageField(upload_to="images", null=True, blank=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
