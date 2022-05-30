from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


from django.http import HttpResponse


from django.http import HttpResponseRedirect

from django_education.models import TextPost


def home(request):
    posts = TextPost.objects.all()
    return render(request, "posts.html", context={"posts": posts})


def delete_last_post(request):
    TextPost.objects.last().delete()
    return HttpResponseRedirect("/home_page/")


def post_detailes(request, id):
    post = TextPost.objects.get(id=id)
    return render(request, "post.html", context={"post": post})
