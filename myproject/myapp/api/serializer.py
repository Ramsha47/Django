from djoser.serializers import UserCreateSerializer
from myapp.models import User
from myapp.models import Meal
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('id', 'email', 'name', 'password')
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'name', 'description', 'price']