from rest_framework import serializers
from .models import UserProfile


class user_serializer(serializers.Serializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
