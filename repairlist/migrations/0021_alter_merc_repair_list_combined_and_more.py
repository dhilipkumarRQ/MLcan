# Generated by Django 4.2.3 on 2023-07-31 05:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("repairlist", "0020_merc_repair_list_mode_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="merc_repair_list",
            name="combined",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="merc_repair_list",
            name="created_datetime",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="merc_repair_list",
            name="description",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="merc_repair_list",
            name="hour_per_cost",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="merc_repair_list",
            name="id_source",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="merc_repair_list",
            name="max_material_cost",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="merc_repair_list",
            name="max_price",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="merc_repair_list",
            name="repair_mode",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="merc_repair_list",
            name="unit_material_cost",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="merc_repair_list",
            name="units",
            field=models.IntegerField(),
        ),
    ]