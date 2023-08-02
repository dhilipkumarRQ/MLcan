from rest_framework import serializers
from .models import City, Province, Container_Type, Container_Height, Container_Length, Container_Year, Yard, Repair_Area, Repair_Type, Account_Type, Damage_Area, Quantity, Comp, Rep,Component,Event,Dam
from customer.models import Customer

class City_Serializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class Province_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class Container_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Container_Type
        fields = ('id','type','inspection_cost')

class Container_Height_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Container_Height
        fields = '__all__'
        
class Container_Length_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Container_Length
        fields = '__all__'

class Container_Year_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Container_Year
        fields = '__all__'

class Yard_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Yard
        fields = '__all__'

class Repair_Area_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Repair_Area
        fields = '__all__'

class Repair_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Repair_Type
        fields = '__all__'

class Damage_Area_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Damage_Area
        fields = '__all__'

class Account_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Type
        fields = '__all__'
        
class Quantity_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = '__all__'

class Comp_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comp
        fields = '__all__'

class Component_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class Rep_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Rep
        fields = '__all__'

class Event_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class Dam_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dam
        fields = '__all__'
