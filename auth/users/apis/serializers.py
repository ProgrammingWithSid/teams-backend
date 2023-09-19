from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import *

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')


class UserOrderSerializer(serializers.ModelSerializer):
    User = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = UserOrder
        fields = '__all__'

    def get_User(self,obj):
        items = obj.user
        serializer = CustomUserCreateSerializer(items,many=False)
        return serializer.data

