from django.shortcuts import render
from rest_framework.decorators import api_view
from mlcan.authentication import authenticate_api
from rest_framework.response import Response
from .serializers import RepairListSerializer,MercRepairListSerializer,NonMercRepairListSerializer
from .models import Merc_Repair_List,Non_Merc_Repair_List,Repair_List
from mlcan.config import MERC_UPDATE,NON_MERC_UPDATE, NON_MERC_TYPE,MERC_TYPE,VERSION_PARAM, MERC_REPAIR_LIST,MERC_REPAIR_LIST_OBJ,NON_MERC_REPAIR_LIST,NON_MERC_REPAIR_LIST_OBJ
from rest_framework import status
from mlcan.pagination import CustomPageNumberPagination
from rest_framework.exceptions import NotFound
import pandas
from json import loads


@api_view(['POST','GET'])
def CreateRepairList(request):
    if request.method == 'POST':
        error, error_message = validate_request_body(request)
        if error:
            return Response(error_message,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        serializer = RepairListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)
    if request.method == 'GET':
        if VERSION_PARAM not in request.query_params:
            raise NotFound("incorrect url, version param missing")
        queryset = Repair_List.objects.filter(version=request.query_params[VERSION_PARAM])
        queryset = get_repair_list(request.query_params, queryset)
        paginator = CustomPageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = RepairListSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
@api_view(['PUT'])
def EditRepairList(request, repair_id):
    if request.method == 'PUT':

        if 'id' not in request.data['repair_list_object']:
            return Response({"data": {}, "success": False, "error": {"message": "id is not present for repair list object"}}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        rl_object = Repair_List.objects.get(id=repair_id)
        if rl_object.repair_list_id != request.data['repair_list_object']['id']:
            return Response({"message": "repair list object id mismatch"})
        if isinstance(rl_object.repair_list_object, Merc_Repair_List):
            request.data['repair_list_object']['repair_serializer_type'] = MERC_UPDATE
        if isinstance(rl_object.repair_list_object, Non_Merc_Repair_List):
            request.data['repair_list_object']['repair_serializer_type'] = NON_MERC_UPDATE 
        merc_non_merc_id = Repair_List.objects.filter(repair_list_id=request.data['repair_list_object']['id']).count()
        if merc_non_merc_id > 1:
            complete_object_serializer = RepairListSerializer(data=request.data)
            if complete_object_serializer.is_valid():
                pass
            else:
                return Response(complete_object_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            repair_data = request.data.pop('repair_list_object', None)
            repair_data.pop('id', None)
            repair_data.pop('version', None)
            if repair_data['repair_serializer_type'] == MERC_UPDATE:
                merc_serializer  = MercRepairListSerializer(data=repair_data)
                if merc_serializer.is_valid():
                    obj = merc_serializer.save()
                    instance = Repair_List.objects.get(id=repair_id)
                    for key, value in request.data.items():
                        setattr(instance, key, value)
                    instance.repair_list_id = obj.id
                    instance.save()
                    return Response(RepairListSerializer(Repair_List.objects.get(id=repair_id)).data)
                else:
                    return Response(merc_serializer.errors)
            if repair_data['repair_serializer_type'] == NON_MERC_UPDATE:
                non_merc_serializer  = NonMercRepairListSerializer(data=repair_data)
                if non_merc_serializer.is_valid():
                    obj = non_merc_serializer.save()
                    instance = Repair_List.objects.get(id=repair_id)
                    for key, value in request.data.items():
                        setattr(instance, key, value)
                    instance.repair_list_id = obj.id
                    instance.save()
                    return Response(RepairListSerializer(Repair_List.objects.get(id=repair_id)).data)
                else:
                    return Response(non_merc_serializer.errors)
            
        else:
            repair_list_serializer = RepairListSerializer(instance=rl_object, data=request.data)
            if repair_list_serializer.is_valid():
                repair_list_serializer.save()
                return Response(repair_list_serializer.data)
            else:
                return Response(repair_list_serializer.errors)


@api_view(['POST'])
def AddVersion(request):
    if request.method == 'POST':
        repairlist_objects = Repair_List.objects.all()
        current_version = get_max_current_version(repairlist_objects)
        repairlist_objects = repairlist_objects.filter(version=current_version)
        modified_repairlist_objects = []
        for object in repairlist_objects:
            object.version = current_version+1
            object.id = None
            modified_repairlist_objects.append(object)
        queryset = Repair_List.objects.bulk_create(modified_repairlist_objects)
        queryset = get_repair_list(request.query_params, queryset)
        if not queryset:
            return Response(
                    {
                        "data": {},
                        "message": "no results found",
                        "success": True,
                    }, 
                    status=status.HTTP_200_OK)
        paginator = CustomPageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = RepairListSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)      

@api_view(['POST'])
def BulkUpload(request):
    if request.method == 'POST':
        file_obj = request.data['repairlist']
        file_content = file_obj.read()
        excel_data_df = pandas.read_excel(file_content,engine='openpyxl')
        result = loads(excel_data_df.to_json(orient='records'))
        repair_list = []
        for record in result:
            temp_dict = {"repair_list_object": {}}
            common_fields = None
            repair_list_fields = None
            if record['repair_serializer_type'] == MERC_TYPE:
                common_fields = MERC_REPAIR_LIST
                repair_list_fields = MERC_REPAIR_LIST_OBJ
            if record['repair_serializer_type'] == NON_MERC_TYPE:
                common_fields = NON_MERC_REPAIR_LIST
                repair_list_fields = NON_MERC_REPAIR_LIST_OBJ
            for key in record.keys():
                if key in common_fields:
                    temp_dict[key] = record[key]
                if key in repair_list_fields:
                    temp_dict['repair_list_object'][key] = record[key]
            repair_list.append(temp_dict)
        serializer = RepairListSerializer(data=repair_list,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    {
                        "data": serializer.data,
                        "message": "repair list bulk upload successfuly",
                        "success": True,
                    }, 
                    status=status.HTTP_201_CREATED)
        else:
            return Response(
                    {
                        "data": serializer.errors,
                        "message": "error in bulk uploading",
                        "success": False,
                    }, 
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)



def validate_request_body(request):
    if 'repair_serializer_type' not in request.data['repair_list_object'].keys():
        return [True, {"data": {}, "success": False, "error": {"message": "repair_serializer_type field missing"}}]
    if request.data['repair_list_object']['repair_serializer_type'] != MERC_TYPE and request.data['repair_list_object']['repair_serializer_type'] != NON_MERC_TYPE:
        return [True, {"data": {}, "success": False, "error": {"message": "repair_serializer_type field value incorrect"}}]              
    return [False, None]

def get_max_current_version(queryset):
    return queryset.order_by('-version').first().version

def get_repair_list(query_params, queryset):
    if 'search' in query_params:
        queryset = queryset.filter(repair_id__contains=query_params['search'])
    if 'repair_area' in query_params:
        queryset = queryset.filter(container_repair_area__area=query_params['repair_area'])
    if 'damage_area' in query_params:
        queryset = queryset.filter(container_damaged_area__area=query_params['damage_area'])
    if 'repair_type' in query_params:
        queryset = queryset.filter(repair_type__type=query_params['repair_type'])
    return queryset