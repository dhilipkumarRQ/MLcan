# Generated by Django 4.2.3 on 2023-07-24 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("meta", "0013_rename_city_id_yard_city"),
        ("activity", "0007_activity_quote_repair_list_activity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity_quote_repair_attachment",
            name="activity_quote_repair_list",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="activity.activity_quote_repair_list",
            ),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_attachment",
            name="area",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="meta.repair_area",
            ),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_attachment",
            name="attachment_path",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_attachment",
            name="attachment_type",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_attachment",
            name="created_datetime",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="activity_quote_repair_attachment",
            name="modified_datetime",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
