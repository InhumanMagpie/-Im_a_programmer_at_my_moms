from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import TextPostViewSet, ImagePostViewSet, AuthorViewSet, CommentsViewSet, AuthorInfoViewSet

router = DefaultRouter()
router.register(r"posts/text", TextPostViewSet, basename="text")
router.register(r"posts/image", ImagePostViewSet, basename="image")
router.register(r"authors", AuthorViewSet, basename="authors")
router.register(r"authors/info", AuthorInfoViewSet, basename="authors_info")
router.register(r"comments", CommentsViewSet, basename="comments")
urlpatterns = router.urls
