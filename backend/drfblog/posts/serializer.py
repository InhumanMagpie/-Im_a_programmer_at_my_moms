from rest_framework import serializers

from posts.models import Comments, ImagePost, TextPosts, Author, AuthorInfo


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class TextPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPosts
        fields = "__all__"


class ImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["username", "email", "password", "info"]


class AuthorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorInfo
        fields = "__all__"
