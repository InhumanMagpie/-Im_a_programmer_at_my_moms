from datetime import datetime

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from django_education.forms import PostForm
from django_education.models import TextPost


def home(request):
    posts = TextPost.objects.all()
    return render(request, "posts.html", context={"posts": posts})


def post_details(request, id):
    post = TextPost.objects.get(id=id)
    form = PostForm(instance=post)
    return render(request, "post.html", context={"form": form})


def add_post(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect("/django_education/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, "add_posts.html", {"form": form})


def delete_post(request, id):
    post = TextPost.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect("/django_education/")


# class PostListView(ListView):
#     model = TextPost
#     template_name = 'posts.html'
#     context_object_name = 'posts'
#
# class PostEditView(UpdateView):
#     model = TextPost
#     template_name = 'edit_post.html'
#     form_class = PostForm
#     success_url = '/demo/posts'
#
# class PostCreateView(CreateView):
#     model = TextPost
#     template_name = 'add_post.html'
#     form_class = PostForm
#     success_url = '/demo/posts'
#
# class PostDeleteView(DeleteView):
#     model = TextPost
#     template_name = 'delete_post.html'
#     success_url = '/demo/posts'
#
# def delete_post(request, id):
#     post = TextPost.objects.get(id=id)
#     post.delete()
#     return HttpResponseRedirect('/demo/posts')
