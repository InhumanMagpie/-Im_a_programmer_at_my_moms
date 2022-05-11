from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from django_aducation.models import Person


def post_list(request):
    return render(request, 'blog/post_list.html', {})


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def show_user(request):
    user = Person.objects.all()
    context = {"user": list(user)}
    return JsonResponse(context)
