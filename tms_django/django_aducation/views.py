from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# from django_aducation.models import Person

from django.http import HttpResponse


def home(request):
    return render(request, "home_page.html")


def about_us(request):
    return render(request, "about_us.html")


def our_partners(request):
    return render(request, "our_partners.html")
