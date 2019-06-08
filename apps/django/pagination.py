from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response
from collections import OrderedDict


class MyPagination(PageNumberPagination):

    def get_page_size(self, request):
        page_size = request.GET.get('limit')
        if page_size:
            return page_size
        return super(MyPagination, self).get_page_size(request)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('pages', self.page.paginator.num_pages),
            ('current_page', self.page.number),
            ('results', data)
        ]))
