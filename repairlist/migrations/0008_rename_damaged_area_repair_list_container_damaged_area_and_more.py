# Generated by Django 4.2.3 on 2023-07-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("repairlist", "0007_rename_damage_area_non_merc_repair_list_damaged_area"),
    ]

    operations = [
        migrations.RenameField(
            model_name="repair_list",
            old_name="damaged_area",
            new_name="container_damaged_area",
        ),
        migrations.RenameField(
            model_name="repair_list",
            old_name="repair_area",
            new_name="container_repair_area",
        ),
        migrations.AlterField(
            model_name="repair_list",
            name="created_datetime",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="repair_list",
            name="repair_code",
            field=models.IntegerField(),
        ),
    ]