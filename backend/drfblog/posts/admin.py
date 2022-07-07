from django.contrib import admin

# Register your models here.
from posts.models import Author, AuthorInfo, TextPosts, ImagePost, Comments

admin.site.register(Author)
admin.site.register(AuthorInfo)
admin.site.register(TextPosts)
admin.site.register(ImagePost)
admin.site.register(Comments)
