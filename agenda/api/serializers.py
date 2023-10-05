from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserModelSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = User
        fields = ("id","username", "password", "email")

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)


class ContactModelSerializer(serializers.ModelSerializer):
    """Contact model serializer"""

    class Meta:
        model = models.Contact
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "user",
        )