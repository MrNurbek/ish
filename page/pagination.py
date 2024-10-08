from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination
from rest_framework.response import Response


class YourPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class LargeResultsSetPagination(YourPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CustomResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000
