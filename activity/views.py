from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CommentSerializer
from rest_framework import status
from mlcan.config import COMMENT_ORIGIN_ALLOWED
from django.http import HttpResponse



@api_view(['POST'])
def CreateComment(request):
    if 'comment_origin' not in request.data or request.data['comment_origin'] not in COMMENT_ORIGIN_ALLOWED:
        return Response({
                    "data": {},
                    "message": "invalid / missing comment_origin",
                    "success": False,
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    serializer = CommentSerializer(data=request.data)
    print(f'{type(request.data)=}')
    print(f'{request.data=}')
    if serializer.is_valid():
        extra_data = {
            'comment_origin': request.data['comment_origin'],
            'comment_origin_id': request.data['comment_origin_id']
        }
        serializer.validated_data.update(extra_data)
        serializer.save()
        return Response(serializer.data)    
    return Response("post method")
        

@api_view(['GET'])
def Comment(request):
    return Response("get method")

