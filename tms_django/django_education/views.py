from datetime import datetime

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from django_education.forms import PostForm
from django_education.models import Letter


class PostListMails(ListView):
    model = Letter
    template_name = "mails.html"
    context_object_name = "mails"


# class PostEditView(UpdateView):
#     model = TextPost
#     template_name = "edit_mail.html"
#     form_class = PostForm
#     success_url = "/demo/posts"


class PostCreateMail(CreateView):
    model = Letter
    template_name = "add_mail.html"
    form_class = PostForm
    success_url = "/django_education/mails"


# class PostDeleteView(DeleteView):
#     model = TextPost
#     template_name = "delete_post.html"
#     success_url = "/demo/posts"


# def delete_post(request, id):
#     post = TextPost.objects.get(id=id)
#     post.delete()
#     return HttpResponseRedirect("/demo/posts")
