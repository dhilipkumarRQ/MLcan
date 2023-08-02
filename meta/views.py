from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Container_Type_Serializer, Container_Height_Serializer, Container_Length_Serializer,Container_Year_Serializer, City_Serializer, Province_Serializer, Damage_Area_Serializer,Repair_Area_Serializer, Repair_Type_Serializer, Yard_Serializer, Account_Type_Serializer, Quantity_Serializer
from .models import Container_Type, Container_Height, Container_Length, Container_Year,City,Province,Damage_Area,Repair_Area,Repair_Type,Yard,Quantity,Account_Type

@api_view(['GET'])
def Get_Container_Type(request):
    if request.method == 'GET':
        query_set = Container_Type.objects.all()
        serialzer = Container_Type_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def Get_Container_Height(request):
    if request.method == 'GET':
        query_set = Container_Height.objects.all()
        serialzer = Container_Height_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def Get_Container_Length(request):
    if request.method == 'GET':
        query_set = Container_Length.objects.all()
        serialzer = Container_Length_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def Get_Container_Year(request):
    if request.method == 'GET':
        query_set = Container_Year.objects.all()
        serialzer = Container_Year_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def Get_City(request):
    if request.method == 'GET':
        query_set = City.objects.all()
        serialzer = City_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def Get_Province(request):
    if request.method == 'GET':
        query_set = Province.objects.all()
        serialzer = Province_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def Get_Damage_Area(request):
    if request.method == 'GET':
        query_set = Damage_Area.objects.all()
        serialzer = Damage_Area_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def Get_Repair_Area(request):
    if request.method == 'GET':
        query_set = Repair_Area.objects.all()
        serialzer = Repair_Area_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def Get_Repair_Type(request):
    if request.method == 'GET':
        query_set = Repair_Type.objects.all()
        serialzer = Repair_Type_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def Get_Yard(request):
    if request.method == 'GET':
        query_set = Yard.objects.all()
        serialzer = Yard_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def Get_Quantity(request):
    if request.method == 'GET':
        query_set = Quantity.objects.all()
        serialzer = Quantity_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def Get_Account_Type(request):
    if request.method == 'GET':
        query_set = Account_Type.objects.all()
        serialzer = Account_Type_Serializer(query_set, many=True)
        return Response({'data': serialzer.data, 'success': True, 'message': 'successfuly retrieved'}, status=status.HTTP_200_OK)

