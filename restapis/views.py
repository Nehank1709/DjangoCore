from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BoookSerializer

# Create your views here.

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BoookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BoookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


