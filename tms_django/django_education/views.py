from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# from django_education.models import Person

from django.http import HttpResponse

from django_education.models import Blog
from django.http import HttpResponseRedirect


def home(request):
    posts = Blog.objects.all()
    return render(request, "posts.html", context={"posts": posts})


def delete_last_post(request):
    Blog.objects.last().delete()
    return HttpResponseRedirect("/home_page/")


def post_detailes(request, id):
    post = Blog.objects.get(id=id)
    return render(request, "post.html", context={"post": post})
