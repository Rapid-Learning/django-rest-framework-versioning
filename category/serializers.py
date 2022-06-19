from dataclasses import field
from .models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         """
#         Create and return a new `Category` instance, given the validated data.
#         """
#         return Category.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Category` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance
