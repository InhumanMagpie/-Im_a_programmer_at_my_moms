import time

import django_filters
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from posts.models import Author, AuthorInfo, TextPosts, ImagePost, Comments
from posts.serializer import (
    AuthorSerializer,
    TextPostSerializer,
    ImagePostSerializer,
    CommentsSerializer,
    AuthorInfoSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["username"]
    search_fields = ["username", "email"]

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        time.sleep(3)
        return super().list(request, *args, **kwargs)


class AuthorInfoViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorInfoSerializer
    queryset = AuthorInfo.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["birthday", "country"]
    search_fields = ["birthday", "country"]


class TextPostViewSet(viewsets.ModelViewSet):
    serializer_class = TextPostSerializer
    queryset = TextPosts.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["title"]
    search_fields = ["title"]


class ImagePostViewSet(viewsets.ModelViewSet):
    serializer_class = ImagePostSerializer
    queryset = ImagePost.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["title"]
    search_fields = ["title"]


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["create_at"]
    search_fields = ["create_at"]
