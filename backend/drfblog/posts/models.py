from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class AuthorInfo(models.Model):
    birthday = models.DateField()
    country = models.TextField()
    city = models.TextField()


class Author(User):
    info = models.OneToOneField(
        AuthorInfo, on_delete=models.CASCADE, null=True, blank=True
    )


class BasePost(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateField(auto_now_add=True)
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(
        Author, related_name="post_author", on_delete=models.CASCADE
    )


class TextPosts(BasePost):
    pass


class ImagePost(TextPosts):
    image = models.ImageField(upload_to="ImagePost")


class Comments(models.Model):
    owner = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(TextPosts, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
