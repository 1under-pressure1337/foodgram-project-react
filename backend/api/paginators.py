from rest_framework.pagination import PageNumberPagination

PAGE_SIZE = 3


class PageLimitPagination(PageNumberPagination):
    page_size_query_param = PAGE_SIZE
