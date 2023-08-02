from rest_framework import pagination
from rest_framework.response import Response 

class CustomPageNumberPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'data': {
                'results': data,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'total_count': self.page.paginator.count,
                'current_page': self.page.number
            },
            "success": True,
            "message": "successfully retrieved customer"
        })

