"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django_aducation import views
from django_project import settings

urlpatterns = [
    path('', views.home, name="home_page"),
    path('about_us/', TemplateView.as_view(template_name="home_page.html"), name="home_page"),
    path('post_1/', TemplateView.as_view(template_name="post_1.html"), name="post_1"),
    path('post_2/', TemplateView.as_view(template_name="post_2.html"), name="post_2")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
