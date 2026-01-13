from rest_framework.pagination import PageNumberPagination

class DoctorPagination(PageNumberPagination):
    page_size = 5  # એક પેજ પર કેટલા ડોક્ટર બતાવવા છે
    page_size_query_param = 'page_size'
    max_page_size = 100