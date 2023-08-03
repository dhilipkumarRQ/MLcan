from django.db import models
from meta.models import Yard,Container_Height, Container_Length, Container_Year, Container_Type
from customer.models import Customer
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation

class Container(models.Model):
    yard = models.ForeignKey(Yard,on_delete=models.CASCADE)
    container_no = models.IntegerField(unique=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    submitter_initials = models.CharField(max_length=50)
    height = models.ForeignKey(Container_Height, on_delete=models.SET_NULL, null=True)
    length = models.ForeignKey(Container_Length, on_delete=models.SET_NULL, null=True)
    manufacture_year = models.ForeignKey(Container_Year, on_delete=models.SET_NULL, null=True)
    container_type = models.ForeignKey(Container_Type, related_name="container", on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=timezone.now)
    comments = GenericRelation('activity.Comment')

class Container_Attachment(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE, related_name='container_attachment')
    attachment_name = models.CharField(max_length=20)
    attachment_path = models.ImageField(max_length=200, blank=True,null=True,upload_to='images/container/%y/%m/%d')
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=timezone.now)




