from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  
from .serializers import ContainerSerializer
from mlcan.config import COMMENT_ORIGIN_ALLOWED, COMMENT_TYPE, CONTAINER_IMAGE_TYPE, CONTAINER_FILTER_FIELDS
from activity.serializers import CommentSerializer
from django.http import QueryDict
from mlcan.authentication import get_payload_from_token,authenticate_api
from .models import Container
from mlcan.pagination import CustomPageNumberPagination
from django.db.models import Q


@api_view(['GET','POST'])
@authenticate_api
def GetAddContiner(request):
    
    if request.method == 'GET':
        paginator = CustomPageNumberPagination()
        if 'page_size' in request.GET:
            paginator.page_size = int(request.GET.get('page_size'))
        query_set = Container.objects.all()
        container_objects = get_all_containers(request.query_params, query_set)
        if not container_objects:
            return Response(
                    {
                        "data": {},
                        "message": "no results found",
                        "success": True,
                    }, 
                    status=status.HTTP_200_OK)
        result_page = paginator.paginate_queryset(container_objects, request)
        serializer = ContainerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    if isinstance(request.data, QueryDict):
        request.data._mutable = True
        modify_request_body(request) 
        query_dict = request.data
        data_dict = {key: query_dict.getlist(key) if len(query_dict.getlist(key)) > 1 else query_dict[key] for key in query_dict.keys()}
    if request.method == 'POST':
        if not check_request_contains_all_photo(request):
            return Response('container_images missing')
        serializer = ContainerSerializer(data=data_dict)
        if serializer.is_valid():
            serializer.save()
            modify_request_body(request, serializer.data['id']) 
            comment_serializer = CommentSerializer(data=request.data['comment'])
            if comment_serializer.is_valid():
                extra_data = {
                    'comment_origin': request.data['comment']['comment_origin'],
                    'comment_origin_id': request.data['comment']['comment_origin_id']
                }
                comment_serializer.validated_data.update(extra_data)
                comment_serializer.save()
                # implement transactions
            else:
                return Response(
                    {"data": {}, "success": False, "error": {"message": serializer.errors}},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )
                
            return Response(
                {
                    "data": serializer.data,
                    "message": "container created successfuly",
                    "success": True,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"data": {}, "success": False, "error": {"message": serializer.errors}},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
    

@api_view(['GET','PUT'])
def GetContainer(request, container_id):
    queryset = Container.objects.filter(id=container_id).first()
    if not queryset:
        return Response(
                    {
                        "data": {},
                        "message": "container not found",
                        "success": False,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

    if request.method == 'GET':
        serializer = ContainerSerializer(queryset)
        return Response(
                {
                    "data": serializer.data,
                    "message": "container retrieved successfully",
                    "success": True,
                },
                status=status.HTTP_200_OK,
            )
            
    if isinstance(request.data, QueryDict):
        request.data._mutable = True
        modify_request_body(request) 
        query_dict = request.data
        data_dict = {key: query_dict.getlist(key) if len(query_dict.getlist(key)) > 1 else query_dict[key] for key in query_dict.keys()}
    if request.method == 'PUT':
        if not check_request_contains_all_photo(request):
            return Response('container_images missing')
        serializer = ContainerSerializer(instance=queryset,data=data_dict,partial=False)
        if serializer.is_valid():
            serializer.save()
            # modify_request_body(request, serializer.data['id']) 
            # comment_serializer = CommentSerializer(data=request.data['comment'])
            # if comment_serializer.is_valid():
            #     extra_data = {
            #         'comment_origin': request.data['comment']['comment_origin'],
            #         'comment_origin_id': request.data['comment']['comment_origin_id']
            #     }
            #     comment_serializer.validated_data.update(extra_data)
            #     comment_serializer.save()
            #     # implement transactions
            # else:
            #     return Response(
            #         {"data": {}, "success": False, "error": {"message": serializer.errors}},
            #         status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            #     )
                
            return Response(
                {
                    "data": serializer.data,
                    "message": "container created successfuly",
                    "success": True,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"data": {}, "success": False, "error": {"message": serializer.errors}},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
    

def modify_request_body(request, container_id=None):
    request.data['comment'] = {
        "user_id": get_payload_from_token(request)["id"],
        "comment_origin": COMMENT_ORIGIN_ALLOWED[0],
        "comment_origin_id": container_id,
        "comment_type": COMMENT_TYPE.CONTAINER.value,
        'comment_text': request.data['comment_text']
    }
    images = []
    for image_type in CONTAINER_IMAGE_TYPE:
        images.append({'attachment_name':image_type.value,
                       'attachment_path': request.data.get(image_type.value, None)
                       })
    request.data['container_attachment'] = images

def check_request_contains_all_photo(request):
    image_enum = set(item.value for item in CONTAINER_IMAGE_TYPE)
    request_keys = set(request.data.keys())
    if image_enum.issubset(request_keys):
        return True
    return False
    
def get_all_containers(query_params, query_set):
    if 'search' in query_params:
        return query_set.filter(Q(container_no__icontains=query_params['search'])|Q(id__icontains=query_params['search']))
    return query_set