from django.contrib.auth.models import Permission
from rest_framework import serializers

from teamwork.models import User, Team


class CustomSerializer(serializers.Serializer):
    field_1 = serializers.CharField(write_only=True)
    field_2 = serializers.JSONField(read_only=True, default="Hello")


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    my_field = serializers.SerializerMethodField()
    perms = PermissionSerializer(many=True, source="user_permissions")

    class Meta:
        model = User
        fields = (
            "id",
            "slug",
            "username",
            "role",
            "team",
            "status",
            "count_tasks",
            "my_field",
            "perms",
        )

    def get_my_field(self, instance):
        return {"a": 2, "hello": "world"}


class TeamSerializer(serializers.ModelSerializer):
    manager = UserSerializer(many=False)
    employers = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = ("id", "name", "manager", "employers")
