from dataclasses import field
from .models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CategorySerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']