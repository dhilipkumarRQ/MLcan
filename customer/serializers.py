from rest_framework import serializers
from .models import Customer
from rest_framework.exceptions import ValidationError 
from django.contrib.auth.hashers import make_password
from meta.models import City, Province, Container_Type
from meta.serializers import City_Serializer, Province_Serializer, Container_Type_Serializer


class CustomerSerializer(serializers.ModelSerializer):

    city_id = serializers.PrimaryKeyRelatedField(queryset = City.objects.all(), source='city', write_only=True)
    city = City_Serializer(read_only=True)

    province_id  = serializers.PrimaryKeyRelatedField(queryset = Province.objects.all(), source = 'province',write_only=True)
    province = Province_Serializer(read_only=True)

    repair_list_type_id = serializers.PrimaryKeyRelatedField(queryset = Container_Type.objects.all(), source='repair_list_type',write_only=True)
    repair_list_type = Container_Type_Serializer(read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id','name','email','password','owner_name','billing_name', 'hourly_rate','gst','pst',"city_id","city",'province_id','province','address','postal_code','repair_list_type_id','repair_list_type','active_state','modified_datetime','created_datetime']
        extra_kwargs = {
            'password': {'write_only': True},
        }


    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("password should contain min of 8 character")
        if value.isnumeric():
            raise ValidationError("password should atleast contains alphabet")
        if value.isalpha():
            raise ValidationError("password should atleast contains numbers")
        return make_password(value)
    
    def validate_email(self, value):
        if '@gmail.com' not in value:
            raise ValidationError("enter valid email address")
        return value
        



