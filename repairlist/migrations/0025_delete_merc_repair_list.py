# Generated by Django 4.2.3 on 2023-07-31 05:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("repairlist", "0024_remove_merc_repair_list_created_datetime_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Merc_Repair_List",
        ),
    ]
