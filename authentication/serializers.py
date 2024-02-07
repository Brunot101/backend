from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        return data
