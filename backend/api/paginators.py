from rest_framework.pagination import PageNumberPagination

PAGE_LIMIT = 3


class PageLimitPagination(PageNumberPagination):
    page_size_query_param = PAGE_LIMIT

# 1
