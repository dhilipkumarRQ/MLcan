# Generated by Django 4.2.3 on 2023-08-01 01:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("repairlist", "0028_alter_merc_repair_list_combined"),
    ]

    operations = [
        migrations.RenameField(
            model_name="repair_list",
            old_name="repair_code",
            new_name="primary_repair_code",
        ),
    ]
