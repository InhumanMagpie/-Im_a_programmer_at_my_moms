from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# from django_aducation.models import Person

from django.http import HttpResponse


def home(request):
    return render(request, "home_page.html")


def post_1(request):
    return render(request, "post_1.html")


def post_2(request):
    return render(request, "post_2.html")
