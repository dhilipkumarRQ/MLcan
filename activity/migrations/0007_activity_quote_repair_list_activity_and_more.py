# Generated by Django 4.2.3 on 2023-07-24 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("repairlist", "0001_initial"),
        ("meta", "0013_rename_city_id_yard_city"),
        (
            "activity",
            "0006_activity_log_container_activity_log_created_datetime_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="activity",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="activity.activity_ledger",
            ),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="activity_type",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="comment",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="created_datetime",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="location",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="modified_datetime",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="quantity",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="meta.quantity",
            ),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="repair",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="repairlist.repair_list",
            ),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="repair_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="meta.repair_type",
            ),
        ),
    ]
