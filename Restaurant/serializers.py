from django.contrib.auth.models import User
from . models import Menu, Book
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BooKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'