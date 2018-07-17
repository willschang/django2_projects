from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from .api import APIResponse


# 自定义 rest_framework 分布设置
class CustomPaginationSerializer(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100

    def get_paginated_data(self, data):
        return OrderedDict([
            ('total_count', self.page.paginator.count),
            ('total_page', self.page.paginator.num_pages),
            ('current_page', self.page.number),
            ('results', data)
        ])

    def get_paginated_response(self, data):
        return APIResponse(self.get_paginated_data(data))

