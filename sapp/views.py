from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Book
# Create your views here.
class BookView(APIView):
    def get(self, request, format=None):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        