from rest_framework import serializers
from .models import Comment, Activity_Quote_Repair_List,Activity_Ledger, Activity_Quote_Repair_Attachment,Activity_Timeline
from account.models import User
from container.models import Container
from repairlist.models  import Repair_List
from account.serializers import UserSerializers
from mlcan.config import COMMENT_ORIGIN_ALLOWED
from meta.models import Repair_Type, Quantity
from meta.serializers import Quantity_Serializer
from repairlist.serializers import RepairListSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        user_obj = User.objects.get(id=obj.user_id)
        user_ser = UserSerializers(user_obj).data
        user_ser.pop('password')
        return user_ser

    class Meta:
        model=Comment
        fields = ['id','user_id','user','comment_text','comment_type','modified_datetime']
        

    def create(self, validated_data):
        object = None
        if validated_data['comment_origin'] == COMMENT_ORIGIN_ALLOWED[0]:
            object = Container.objects.filter(id=validated_data['comment_origin_id']).first()
        else:
            object = Activity_Quote_Repair_List.objects.filter(id=validated_data['comment_origin_id']).first()
        validated_data.pop('comment_origin')
        validated_data.pop('comment_origin_id')
        return Comment.objects.create(content_object=object,**validated_data)
    
class ActivityQuoteRepairListAttachmentSerializer(serializers.ModelSerializer):
    activity_quote_repair_list = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Activity_Quote_Repair_Attachment
        fields = ['id','activity_quote_repair_list','repair_area_attachment','damaged_area_attachment','created_datetime','modified_datetime']

    
class ActivityQuoteRepairListSerializer(serializers.ModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(queryset = Activity_Ledger.objects.all(), source='activity',write_only=True)
    repair_id = serializers.PrimaryKeyRelatedField(queryset = Repair_List.objects.all(), source='repair',write_only=True)
    repair_type_id = serializers.PrimaryKeyRelatedField(queryset = Repair_Type.objects.all(), source = 'repair_type',write_only=True)
    quantity_id = serializers.PrimaryKeyRelatedField(queryset = Quantity.objects.all(), source='quantity',write_only=True)
    quantity = Quantity_Serializer(read_only=True)
    repair = RepairListSerializer(read_only=True)
    activity = serializers.PrimaryKeyRelatedField(read_only=True)
    # attachment = ActivityQuoteRepairListAttachmentSerializer()
    class Meta:
        model = Activity_Quote_Repair_List
        fields = ['id','activity_id','activity','repair_id','repair','repair_type_id','repair_type','quantity_id','quantity','location','activity_type','comment','created_datetime','modified_datetime']

    # def create(self, validated_data):
    #     activity_attachment_validated_data = validated_data.pop('attachment')
    #     obj =  Activity_Quote_Repair_List.objects.create(**validated_data)
    #     Activity_Quote_Repair_Attachment.objects.create(act_quote_repair_list=obj,**activity_attachment_validated_data)
    #     return obj


class ActivityTimelineSerializer(serializers.ModelSerializer):

    activity = serializers.PrimaryKeyRelatedField(queryset= Activity_Ledger.objects.all(), required=False)
    class Meta:
        model =  Activity_Timeline
        fields = '__all__'

class ActivityLedgerSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    container_id = serializers.PrimaryKeyRelatedField(queryset=Container.objects.all(), source = 'container', write_only=True)
    activity_timeline = ActivityTimelineSerializer(many=True)

    repair_list = serializers.SerializerMethodField()

    def get_repair_list(self, obj):
        repair_list_obj = Activity_Quote_Repair_List.objects.filter(activity_id=obj.id)
        return ActivityQuoteRepairListSerializer(repair_list_obj,many=True).data

    class Meta:
        model=Activity_Ledger
        fields = ['id','user_id','container_id','activity_type','activity_timeline','activity_date','repair_list','status','modified_datetime']
    
    def create(self, validated_data):
        timelines = validated_data.pop('activity_timeline')
        activity = Activity_Ledger.objects.create(**validated_data)
        for timeline in timelines:
            Activity_Timeline.objects.create(activity=activity, **timeline)
        return activity