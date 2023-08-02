from rest_framework import serializers
from .models import Container, Container_Attachment
from meta.models import Yard,Container_Height,Container_Length,Container_Type,Container_Year
from customer.models import Customer
from meta.serializers import Container_Type_Serializer, Container_Height_Serializer,Yard_Serializer, Container_Length_Serializer, Container_Year_Serializer
from customer.serializers import CustomerSerializer
from activity.serializers import CommentSerializer


class ContainerAttachmentSerializer(serializers.ModelSerializer):
    container_id = serializers.PrimaryKeyRelatedField(source='container', read_only=True)
    id = serializers.IntegerField(required=False, read_only=False)
    class Meta:
        model = Container_Attachment
        fields = ['id','container_id','attachment_name','attachment_path','created_datetime','modified_datetime']

class ContainerSerializer(serializers.ModelSerializer):

    
    yard_id = serializers.PrimaryKeyRelatedField(queryset=Yard.objects.all(), source='yard',write_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer',write_only=True)
    height_id = serializers.PrimaryKeyRelatedField(queryset=Container_Height.objects.all(), source='height',write_only=True)
    length_id = serializers.PrimaryKeyRelatedField(queryset=Container_Length.objects.all(),source='length',write_only=True)
    manufacture_year_id = serializers.PrimaryKeyRelatedField(queryset=Container_Year.objects.all(), source='manufacture_year',write_only=True)
    container_type_id = serializers.PrimaryKeyRelatedField(queryset=Container_Type.objects.all(), source='container_type',write_only=True)

    yard = Yard_Serializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    height = Container_Height_Serializer(read_only=True)
    length = Container_Length_Serializer(read_only=True)
    manufacture_year =  Container_Year_Serializer(read_only=True)
    container_type = Container_Type_Serializer(read_only=True)

    container_attachment = ContainerAttachmentSerializer(many=True)
    class Meta:
        model = Container
        fields = ['id', 'yard_id',"yard",'container_no', 'customer_id',"customer",'submitter_initials', 'height_id',"height",'length_id',"length",'manufacture_year_id',"manufacture_year",'container_type_id',"container_type",'location','container_attachment']

    def create(self, validated_data):
        attachments = validated_data.pop('container_attachment')
        container_obj =  Container.objects.create(**validated_data)
        for attachment in attachments:
            Container_Attachment.objects.create(container=container_obj, **attachment)     
        return container_obj                                 
    
    def update(self, instance, validated_data): 
        if 'container_attachment' in validated_data:
            container_attachments = validated_data.pop('container_attachment',None)
            container_attachment_instance = instance.container_attachment.all()
            for attachment,attachment_instance in zip(container_attachments,container_attachment_instance):
                for key in attachment.keys():
                    setattr(attachment_instance,key,attachment[key])
                    attachment_instance.save()
        return super(ContainerSerializer, self).update(instance, validated_data)
