from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from category.models import Category
from category.serializers import CategorySerializer, CategorySerializerV2


@api_view(['GET', 'POST'])
def category_list(request, format=None):
    if request.method == 'GET':
        if request.version == 'v1':
            serializer = CategorySerializer
        elif request.version == 'v2':
            serializer = CategorySerializerV2

        categories = Category.objects.all()
        serializer = serializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code category.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
