# Generated by Django 4.2.3 on 2023-07-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="activity_date",
            field=models.DateField(auto_created=True, null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="activity_type",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="created_datetime",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="invoice_date",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="invoice_total",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="modified_datetime",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="parts_cost",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="status",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="subtotal_repair_cost",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="total_cost",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="total_labour_hour",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="total_lobour_cost",
            field=models.FloatField(null=True),
        ),
    ]
