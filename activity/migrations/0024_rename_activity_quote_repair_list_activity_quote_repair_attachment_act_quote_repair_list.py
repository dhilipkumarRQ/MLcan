# Generated by Django 4.2.3 on 2023-08-02 17:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "activity",
            "0023_alter_activity_quote_repair_attachment_damaged_area_attachment_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="activity_quote_repair_attachment",
            old_name="activity_quote_repair_list",
            new_name="act_quote_repair_list",
        ),
    ]
