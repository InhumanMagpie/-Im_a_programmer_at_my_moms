from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ["title", "content", "image_content", "author"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }
