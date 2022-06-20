from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from django_education.models import TextPost, Author


@admin.register(TextPost)
class TextPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "author")
    list_filter = ("created_at", "author")
    search_fields = ("title", "content", "id", "author_name")
    date_hierarchy = "created_at"

    def preview(self, obj):
        if obj.image_content:
            return mark_safe(
                '<img src="{}" width="100" />'.format(obj.image_content.url)
            )
        return mark_safe("<span>No image</span>")

    def mybasecontent(self, obj):
        return obj.base_content()


class inlineTextPost(admin.StackedInline):
    model = TextPost
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
    inlines = [inlineTextPost]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
