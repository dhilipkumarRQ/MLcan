from django.db import models
from meta.models import Damage_Area,Repair_Area,Repair_Type, Container_Type, Comp,Rep,Dam,Event,Component
from customer.models import Customer
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from mlcan.managers import MyManager


# Create your models here.
class Repair_List(models.Model):
    repair_id = models.IntegerField()
    container_repair_area = models.ForeignKey(Repair_Area, on_delete=models.SET_NULL,null=True)
    container_damaged_area = models.ForeignKey(Damage_Area, on_delete=models.SET_NULL,null=True)
    repair_type = models.ForeignKey(Repair_Type, on_delete=models.SET_NULL,null=True)
    repair_component_type = models.ForeignKey(Container_Type, on_delete=models.SET_NULL,null=True)
    repair_list_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    repair_list_id = models.PositiveIntegerField()
    repair_list_object = GenericForeignKey("repair_list_type", "repair_list_id")
    version = models.IntegerField(default=1, editable=False)
    is_deleted = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    objects = MyManager()


class Customer_Repair_List(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    repair_id = models.IntegerField()
    container_repair_area = models.ForeignKey(Repair_Area, on_delete=models.SET_NULL,null=True)
    container_damaged_area = models.ForeignKey(Damage_Area, on_delete=models.SET_NULL,null=True)
    repair_type = models.ForeignKey(Repair_Type, on_delete=models.SET_NULL,null=True)
    repair_component_type = models.ForeignKey(Container_Type, on_delete=models.SET_NULL,null=True)
    repair_list_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    repair_list_id = models.PositiveIntegerField()
    repair_list_object = GenericForeignKey("repair_list_type", "repair_list_id")
    version = models.IntegerField(default=1, editable=False)
    is_deleted = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)


class Non_Merc_Repair_List(models.Model):
    hours = models.FloatField()
    material_cost = models.FloatField()
    container_section = models.CharField(max_length=30)
    damaged_area = models.CharField(max_length=30)
    repair_type = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    comp = models.ForeignKey(Comp, on_delete=models.SET_NULL, null=True)
    dam = models.ForeignKey(Dam, on_delete=models.SET_NULL, null=True)
    rep = models.ForeignKey(Rep, on_delete=models.SET_NULL, null=True)
    component = models.ForeignKey(Component, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=30)
    lgth_qty_area = models.IntegerField()
    lgth_qty_area2 = models.IntegerField()
    id_source = models.IntegerField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    repairlist = GenericRelation(Repair_List)


class Merc_Repair_List(models.Model):
    max_material_cost = models.FloatField()
    unit_material_cost = models.FloatField()
    hour_per_cost = models.FloatField()
    max_price = models.FloatField()
    units = models.IntegerField()
    repair_mode = models.CharField(max_length=50)
    mode_number = models.IntegerField()
    repair_code = models.IntegerField()
    combined = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    id_source = models.IntegerField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    repairlist = GenericRelation(Repair_List)


