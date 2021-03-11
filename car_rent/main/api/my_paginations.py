from rest_framework.pagination import PageNumberPagination

class PagePagination(PageNumberPagination):
    # default_limit = 1
    # limit_query_param = 'limit'
    # offset_query_param = 'offset'
    # max_limit = 20
    page_size = 3