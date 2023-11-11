from django.contrib.auth.models import User
from . models import Menu, Book
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BooKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'