from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from django_education.models import Letter

admin.site.register(Letter)
