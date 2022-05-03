from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from library.books.serializers import *
import base64
from rest_framework.response import Response
from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser, JSONParser
from rest_framework import pagination
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.vary import vary_on_headers

from rest_framework import status

class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'p'

class CustomPaginationOffset(pagination.LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 50

# class LibraryViewSet(viewsets.ModelViewSet):
#     queryset = Library.objects.all().order_by('id')
#     serializer_class = LibrarySerializer
#     permission_classes = []

#     def list(self, request):
#         library_queryset = Library.objects.filter(id__gt = 0)

#         serializer = LibrarySerializer(library_queryset, many = True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         library_queryset = Library.objects.filter(id = pk)
#         serializer = LibrarySerializer(library_queryset)
#         return Response(serializer.data)

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all().order_by('id')
#     serializer_class = EmployeeSerializer
#     permission_classes = []


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all().order_by('id')
    serializer_class = ThingSerializer
    permission_classes = []


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = []
    #pagination_class = CustomPaginationOffset
    #pagination_class = CustomPagination
    
    # def create(self, request):
    #     print('Self:',dir(self))
    #     print('Request:',dir(request))
    #     print('self.options: ',self.options)
    #     print('self.settings: ',self.settings)
    #     print('self.setup: ',self.setup)
    #     print('self.kwargs: ',self.kwargs)
    #     print('self.args: ',self.args)
    #     print('self.post: ',self.post)
    #     print('request.post: ',request.POST)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

        
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = []

#@method.decorator(vary_on_headers('Authorization',))
class BooksAuthorsViewSet(viewsets.ModelViewSet):
    queryset = BooksAuthors.objects.all()
    serializer_class = BooksAuthorsSerializer
    permission_classes = []