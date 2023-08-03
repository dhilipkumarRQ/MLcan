from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CommentSerializer,ActivityLedgerSerializer,ActivityQuoteRepairListSerializer
from rest_framework import status
from mlcan.config import COMMENT_ORIGIN_ALLOWED, QUOTE_ACTIVITY,INSPECTION_ACTIVITY,REPAIR_ACTIVITY
from django.http import HttpResponse
from .models  import Activity_Ledger,Container,Activity_Quote_Repair_List
from mlcan.config import INSPECTION_ACTIVITY, REPAIR_ACTIVITY, QUOTE_ACTIVITY, QUOTE_STATE_ORDER, REPAIR_STATE_ORDER, INSPECTION_STATE_ORDER,READY_FOR_BILLING,BILLED,ADD_REPAIR_QUOTE,ADD_REPAIR_QUOTE_ATTACHMENTS
from django.db.models import Q
from django.http import QueryDict



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
    if serializer.is_valid():
        extra_data = {
            'comment_origin': request.data['comment_origin'],
            'comment_origin_id': request.data['comment_origin_id']
        }
        serializer.validated_data.update(extra_data)
        serializer.save()
        return Response(serializer.data)    
    return Response("post method")
        

@api_view(['POST'])
def CreateActivity(request,container_id):
    if request.method == 'POST':
        request.data['container_id'] = container_id
        activity_serialize =  ActivityLedgerSerializer(data=request.data)
        if activity_serialize.is_valid():
            error, error_message = validate_create_activity_request_body(request.data)
            if error:
                return Response({'data':{}, 'message': error_message, 'success': False}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            activity_serialize.save()
            return Response({'data':activity_serialize.data,'message':'activity created sucessfully','success':True}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data':{},'message':activity_serialize.errors,'success':False}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['PUT'])
def EditStatus(request, activity_id):
    if request.method == 'PUT':
        activity_obj = Activity_Ledger.objects.filter(id=activity_id).first()
        if activity_obj is None:
            return Response({'data':{},'message':'activity with this id is not found','success':False}, status=status.HTTP_404_NOT_FOUND)
        ORDER_LIST = []
        if activity_obj.activity_type == INSPECTION_ACTIVITY:
            ORDER_LIST = INSPECTION_STATE_ORDER
        if activity_obj.activity_type == REPAIR_ACTIVITY:
            ORDER_LIST = REPAIR_STATE_ORDER
        if activity_obj.activity_type == QUOTE_ACTIVITY:
            ORDER_LIST = QUOTE_STATE_ORDER
        if 'status' not in request.data:
            return Response({'data':{},'message':'request body does not contains status','success':False}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if request.data['status'] not in ORDER_LIST:
            return Response({'data':{},'message':'incorrect status given','success':False}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if ORDER_LIST.index(activity_obj.status)+1 == ORDER_LIST.index(request.data['status']):
            activity_obj.status = request.data['status']
            activity_obj.save()
            return Response({'data':ActivityLedgerSerializer(activity_obj).data,'message':'activity updated sucessfully','success':True}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data':{},'message':"given status violates status order",'success':False}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
@api_view(['PUT'])
def EditDate(request, activity_id):
    if request.method == 'PUT':
        activity_obj = Activity_Ledger.objects.filter(id=activity_id).first()
        if activity_obj is None:
            return Response({'data':{},'message':'activity with this id is not found','success':False}, status=status.HTTP_404_NOT_FOUND)
        if 'activity_date' not in request.data:
            return Response({'data':{},'message':'request body does not contains status','success':False}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        activity_obj.activity_date = request.data['activity_date']
        activity_obj.save()
        return Response({'data':ActivityLedgerSerializer(activity_obj).data,'message':'activity updated sucessfully','success':True}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def AddQuoteRepair(request, *args, **kwargs):
    if request.method == 'POST':
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
            modify_add_repair_quote_request_body(request) 
            query_dict = request.data
            data_dict = {key: query_dict.getlist(key) if len(query_dict.getlist(key)) > 1 else query_dict[key] for key in query_dict.keys()}
        else:
            data_dict = request.data.copy()
        data_dict['activity_id'] = kwargs.get('activity_id')
        add_quote_serialize = ActivityQuoteRepairListSerializer(data=data_dict)
        if add_quote_serialize.is_valid():
            add_quote_serialize.save()
            return Response({'data':add_quote_serialize.data,'message':'repair details attached to activity','success':True}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data':{},'message':add_quote_serialize.errors,'success':False}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET'])
def GetActivity(request, container_id):
    if request.method == 'GET':
        activity_obj = Activity_Ledger.objects.filter(container_id=container_id).order_by('-modified_datetime')
        serializer = ActivityLedgerSerializer(activity_obj, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def Comment(request, container_id):
    container_obj = Container.objects.filter(id=container_id).first()
    all_comments = []
    if container_obj is None:
        return Response({'data':{},'message':'container with this id is not found','success':False}, status=status.HTTP_404_NOT_FOUND)
    serialize = CommentSerializer(container_obj.comments.all(), many=True)
    all_comments.extend(serialize.data)
    activity_obj = Activity_Ledger.objects.filter(container_id=container_id).order_by('-modified_datetime')
    activity_serializer = ActivityLedgerSerializer(activity_obj, many=True)
    for activity in activity_serializer.data:
        aqr_obj = Activity_Quote_Repair_List.objects.filter(activity_id=activity['id']).first()
        if aqr_obj is not None:
            c_serializer = CommentSerializer(aqr_obj.comments.all(), many=True)
            all_comments.extend(c_serializer.data)            
    return Response({'data':all_comments,'message':'comments are fetched successfully','success':True}, status=status.HTTP_201_CREATED)

def validate_create_activity_request_body(data):
    if data["activity_type"] not in [QUOTE_ACTIVITY,REPAIR_ACTIVITY,INSPECTION_ACTIVITY]:
        return [True,'activity_type is not valid']
    ALL_ACTIVE_LIST = set()
    ALL_ACTIVE_LIST.update(INSPECTION_STATE_ORDER.copy())
    ALL_ACTIVE_LIST.update(REPAIR_STATE_ORDER.copy())
    ALL_ACTIVE_LIST.update(QUOTE_STATE_ORDER.copy())
    ALL_ACTIVE_LIST.remove(READY_FOR_BILLING)
    ALL_ACTIVE_LIST.remove(BILLED)
    current_active_activity = Activity_Ledger.objects.filter(Q(container_id=data['container_id'])&
                                                             Q(status__in = ALL_ACTIVE_LIST))
    if len(current_active_activity) > 0:
        return [True, 'cannot create new activity, already have current activity']
    return [False, None]



def  modify_add_repair_quote_request_body(request):    
    request.data['attachment'] = {}
    request.data['attachment']['repair_area_attachment'] = request.data['repair_area_attachment']
    request.data['attachment']['damaged_area_attachment'] = request.data['damaged_area_attachment']