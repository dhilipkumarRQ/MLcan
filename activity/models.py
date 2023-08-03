from django.db import models
from container.models import Container
from account.models import User
from meta.models import Repair_Type, Quantity, Damage_Area, Repair_Area
from repairlist.models import Repair_List
from invoice.models import Invoice
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.utils import timezone

# Create your models here.

class Activity_Ledger(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    activity_type = models.CharField(max_length=50)
    activity_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='idle')
    modified_datetime = models.DateTimeField(auto_now=True)

class Activity_Timeline(models.Model):
    activity = models.ForeignKey(Activity_Ledger, on_delete=models.CASCADE, related_name='activity_timeline')
    status = models.CharField(max_length=100)
    status_date = models.DateTimeField(null=True)
    activity_type = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

class Activity_Inspection_Attachment(models.Model):
    activity = models.ForeignKey(Activity_Ledger, on_delete=models.CASCADE, null=True)
    attachment_path = models.CharField(max_length=300, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    modified_datetime = models.DateTimeField(auto_now=True)

class Activity_Log(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    log_type = models.CharField(max_length=100, null=True)
    log_type_id = models.ForeignKey(Activity_Ledger, on_delete=models.CASCADE, null=True) # add Invoice also
    current_state = models.CharField(max_length=100, null=True)
    target_state = models.CharField(max_length=100, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)


class Activity_Quote_Repair_List(models.Model):
    activity = models.ForeignKey(Activity_Ledger, on_delete=models.CASCADE)
    repair = models.ForeignKey(Repair_List, on_delete=models.SET_NULL, null=True)
    repair_type = models.ForeignKey(Repair_Type, on_delete=models.SET_NULL, null=True)
    quantity = models.ForeignKey(Quantity, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    comment = models.CharField(max_length=300)
    created_datetime =  models.DateTimeField(auto_now_add=True)
    modified_datetime =  models.DateTimeField(auto_now=True)

    comments = GenericRelation('activity.Comment')



class Activity_Quote_Repair_Attachment(models.Model):
    act_quote_repair_list = models.OneToOneField(Activity_Quote_Repair_List, on_delete=models.CASCADE, null=True)
    repair_area_attachment = models.ImageField(max_length=300,blank=True,null=True,upload_to='images/activity_attachment')
    damaged_area_attachment = models.ImageField(max_length=300,blank=True,null=True,upload_to='images/activity_attachment')
    created_datetime =  models.DateTimeField(auto_now_add=True, null=True)
    modified_datetime =  models.DateTimeField(auto_now=True, null=True)

class Activity_Invoice(models.Model):
    activity = models.ForeignKey(Activity_Ledger, on_delete=models.CASCADE, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
   
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    comment_text = models.CharField(max_length=300)
    comment_type = models.CharField(max_length=300)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=timezone.now)
    
    def __str__(self):
        return self.comment_text
