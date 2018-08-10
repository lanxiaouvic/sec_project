from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Book, Genre
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

class BookList(generics.ListCreateAPIView):
        queryset = Book.objects.all()
        
        serializer_class = BookSerializer
        permission_classes = (IsAdminOrReadOnly, )
        

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
