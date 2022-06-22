from rest_framework import serializers

from django_education.models import Letter


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'
