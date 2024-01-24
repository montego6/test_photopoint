from rest_framework import serializers

from main.models import UserRequest


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ["timestamp", "exchange_rate"]
