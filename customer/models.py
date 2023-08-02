from django.db import models
from django.utils import timezone
from meta.models import City,Province, Container_Type


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=300, blank=False)
    owner_name = models.CharField(max_length=100, blank=False)
    billing_name = models.CharField(max_length=100, blank=False)
    hourly_rate = models.IntegerField(blank=False)
    gst = models.IntegerField(blank=False)
    pst = models.IntegerField(blank=False)
    city = models.ForeignKey(City, related_name='cities', on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    address  = models.CharField(max_length=300, blank=False)
    postal_code = models.IntegerField(blank=False)
    repair_list_type = models.ForeignKey(Container_Type, related_name='customer', on_delete=models.SET_NULL, null=True)
    active_state = models.BooleanField(blank=False)
    created_datetime =  models.DateTimeField(auto_now_add=True)
    modified_datetime =  models.DateTimeField(auto_now=timezone.now)







