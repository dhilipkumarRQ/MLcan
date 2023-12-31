# Generated by Django 4.2.3 on 2023-07-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("repairlist", "0004_non_merc_repair_list_comp_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="merc_repair_list",
            name="combined",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="created_datetime",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="description",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="hour_per_cost",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="id_source",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="max_material_cost",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="max_price",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="modified_datetime",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="repair_mode",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="unit_material_cost",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="merc_repair_list",
            name="units",
            field=models.IntegerField(null=True),
        ),
    ]
