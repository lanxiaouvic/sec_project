from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Book
from .serializers import BookSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        
        serializer = BookSerializer(books, many=True)
      
        return JSONResponse(serializer.data)
