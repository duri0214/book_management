from rest_framework import generics, response, pagination
from .models import Book, Category
from .serializers import CategorySerializer, BookListSerializer, BookSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 3

    def get_paginated_response(self, data):
        return response.Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
            'page_size': self.page_size,
            'range_first': (self.page.number * self.page_size) - self.page_size + 1,
            'range_last': min((self.page.number * self.page_size), self.page.paginator.count),
        })


class BookList(generics.ListAPIView):
    queryset = Book.objects.all().order_by('category')
    serializer_class = BookListSerializer
    pagination_class = StandardResultsSetPagination


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
