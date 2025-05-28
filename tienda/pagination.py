from rest_framework.pagination import PageNumberPagination

class ElectrodomesticoPagination(PageNumberPagination):
    page_size = 2  # Número de objetos por página
    page_size_query_param = 'page_size'
    max_page_size = 100