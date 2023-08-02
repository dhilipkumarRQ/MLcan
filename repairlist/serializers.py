from rest_framework import serializers
from .models import Merc_Repair_List,Non_Merc_Repair_List, Repair_List
from django.contrib.contenttypes.models import ContentType
from generic_relations.relations import GenericRelatedField
from meta.models import Repair_Area,Damage_Area,Repair_Type, Container_Type, Comp,Dam,Rep,Event,Component
from meta.serializers import Repair_Area_Serializer,Damage_Area_Serializer,Repair_Type_Serializer, Container_Type_Serializer, Dam_Serializer, Comp_Serializer, Rep_Serializer, Component_Serializer,Event_Serializer
from rest_framework.fields import Field
from mlcan.config import MERC_TYPE,NON_MERC_TYPE,MERC_UPDATE,NON_MERC_UPDATE


class NonMercRepairListSerializer(serializers.ModelSerializer):
    comp_id = serializers.PrimaryKeyRelatedField(queryset = Comp.objects.all(), source = 'comp', write_only=True)
    dam_id = serializers.PrimaryKeyRelatedField(queryset = Dam.objects.all(), source = 'dam', write_only=True)
    rep_id = serializers.PrimaryKeyRelatedField(queryset = Rep.objects.all(), source = 'rep', write_only=True)
    component_id = serializers.PrimaryKeyRelatedField(queryset = Component.objects.all(), source = 'component', write_only=True)
    event_id = serializers.PrimaryKeyRelatedField(queryset = Event.objects.all(), source = 'event', write_only=True)

    comp = Comp_Serializer(read_only=True)
    dam = Dam_Serializer(read_only=True)
    rep = Rep_Serializer(read_only=True)
    component = Component_Serializer(read_only=True)
    event = Event_Serializer(read_only=True)

    class Meta:
        model = Non_Merc_Repair_List
        fields = ['id','hours','material_cost','container_section','damaged_area','repair_type','description','comp','comp_id','dam','dam_id','rep','rep_id','component','component_id','event','event_id','location','lgth_qty_area','lgth_qty_area2','id_source','modified_datetime']

class MercRepairListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Merc_Repair_List
        fields = ['id','max_material_cost','unit_material_cost','hour_per_cost','max_price','units','repair_mode','mode_number','repair_code','combined','description','id_source','created_datetime','modified_datetime']

class RepairListObjectRelatedField(Field):
    def to_representation(self, object):
        if isinstance(object, Merc_Repair_List):
            serializer = MercRepairListSerializer(object)
        elif isinstance(object, Non_Merc_Repair_List):
            serializer = NonMercRepairListSerializer(object)
        else:
            raise Exception('Unexpected type of tagged object')
        return serializer.data

    def to_internal_value(self, data):
        repair_type = data['repair_serializer_type']
        if repair_type == MERC_TYPE:
            serializer = MercRepairListSerializer(data=data)
        elif repair_type == NON_MERC_TYPE:
            serializer = NonMercRepairListSerializer(data=data)
        elif repair_type == NON_MERC_UPDATE:
                obj = Non_Merc_Repair_List.objects.filter(id=data['id']).first()
                if not obj:
                    raise serializers.ValidationError("non merc repair list not found") 
                serializer = NonMercRepairListSerializer(instance=obj,data=data)
        elif repair_type == MERC_UPDATE:
                obj = Merc_Repair_List.objects.filter(id=data['id']).first()
                if not obj:
                    raise serializers.ValidationError("merc repair list not found") 
                serializer = MercRepairListSerializer(instance=obj,data=data)
        else:
            raise serializers.ValidationError('no repair_serializer_type provided')
        
        if serializer.is_valid():
            obj = serializer.save()
        else:
            raise serializers.ValidationError(serializer.errors)
        return obj
    

class RepairListSerializer(serializers.ModelSerializer):
    
    container_repair_area_id = serializers.PrimaryKeyRelatedField(queryset=Repair_Area.objects.all(), source='container_repair_area', write_only=True)
    container_damaged_area_id = serializers.PrimaryKeyRelatedField(queryset=Damage_Area.objects.all(), source='container_damaged_area', write_only=True)
    repair_type_id = serializers.PrimaryKeyRelatedField(queryset=Repair_Type.objects.all(), source = 'repair_type', write_only=True)
    repair_component_type_id = serializers.PrimaryKeyRelatedField(queryset = Container_Type.objects.all(), source='repair_component_type', write_only=True)

    container_repair_area = Repair_Area_Serializer(read_only=True)
    container_damaged_area = Damage_Area_Serializer(read_only=True)
    repair_type = Repair_Type_Serializer(read_only=True)
    repair_component_type = Container_Type_Serializer(read_only=True)

    repair_list_object = RepairListObjectRelatedField()
    class Meta:
        model = Repair_List
        fields = ['id','repair_id','container_repair_area','container_repair_area_id','container_damaged_area','container_damaged_area_id','repair_type','repair_type_id','repair_component_type','repair_component_type_id','is_deleted','version','modified_datetime','repair_list_object']

    def create(self, validated_data):
        repair_list = validated_data.pop('repair_list_object')
        return Repair_List.objects.create(repair_list_object=repair_list,**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

