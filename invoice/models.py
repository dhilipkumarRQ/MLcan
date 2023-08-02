from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_date = models.DateField(auto_now_add=True, null=True)
    activity_type = models.CharField(max_length=20, null=True)
    activity_date = models.DateField(auto_created=True, null=True)
    total_cost = models.FloatField(null=True)
    status = models.CharField(max_length=20, null=True)
    total_labour_hour = models.FloatField(null=True)
    parts_cost = models.FloatField(null=True)
    total_lobour_cost = models.FloatField(null=True)
    subtotal_repair_cost = models.FloatField(null=True)
    invoice_total = models.FloatField(null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    modified_datetime = models.DateTimeField(auto_now=True)

