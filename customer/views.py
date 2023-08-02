from rest_framework.decorators import api_view
from rest_framework import  status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import CustomerSerializer
from .models import Customer
from mlcan.pagination import CustomPageNumberPagination
from mlcan.authentication import authenticate_api, auth_only_admin, auth_only_emplopyee
from django.db.models import Q


# Create your views here.

@api_view(['POST'])
def AddCustomer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "message": "customer created successfuly",
                    "success": True,
                }, 
                status=status.HTTP_201_CREATED)
        else:
            return Response({
                    "data": {},
                    "message": serializer.errors,
                    "success": False,
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

@api_view(["GET"])
@authenticate_api
@auth_only_admin
def GetAllCustomer(request):
    if request.method == 'GET':
        paginator = CustomPageNumberPagination()
        if 'page_size' in request.GET:
            paginator.page_size = int(request.GET.get('page_size'))
    
        customer_query_sets = Customer.objects.all()
        customer_objects = get_all_customers(request.query_params, customer_query_sets)
        if not customer_objects:
            return Response(
                    {
                        "data": {},
                        "message": "no results found",
                        "success": True,
                    }, 
                    status=status.HTTP_200_OK)
        result_page = paginator.paginate_queryset(customer_objects, request)
        serializer = CustomerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)



@api_view(['GET','PUT'])
def GetCustomer(request, customer_id):
    if request.method == 'GET': 
         customer = Customer.objects.filter(id=customer_id)
         if len(customer)==1:
            serialize =  CustomerSerializer(customer[0], many=False)
            return Response(
                    {
                        "data": serialize.data,
                        "message": "customer retrieved successfuly",
                        "success": True,
                    }, 
                    status=status.HTTP_200_OK)
         else:
            return Response({
                    "data": {},
                    "message": "customer with the id is not found",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        customer = Customer.objects.filter(id=customer_id)
        if len(customer)==1:
            serializer = CustomerSerializer(customer[0], data=request.data)
            print(f'{request.data}=')
            if serializer.is_valid():
                serializer.save()
                print(f'{serializer.data}=')
                return Response(
                    {
                        "data": serializer.data,
                        "message": "customer updated successfuly",
                        "success": True,
                    }, 
                    status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({
                    "data": {},
                    "message": serializer.errors,
                    "success": False,
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            return Response({
                    "data": {},
                    "message": "customer with the id is not found",
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND)



    
def get_all_customers(query_params, query_set):
    if 'search' in query_params:
        return query_set.filter(Q(name__icontains=query_params['search']))
    return Customer.objects.all()