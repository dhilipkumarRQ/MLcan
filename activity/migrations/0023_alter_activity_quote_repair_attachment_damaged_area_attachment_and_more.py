# Generated by Django 4.2.3 on 2023-08-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "activity",
            "0022_remove_activity_quote_repair_attachment_damaged_area_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity_quote_repair_attachment",
            name="damaged_area_attachment",
            field=models.ImageField(
                blank=True,
                max_length=300,
                null=True,
                upload_to="images/activity_attachment",
            ),
        ),
        migrations.AlterField(
            model_name="activity_quote_repair_attachment",
            name="repair_area_attachment",
            field=models.ImageField(
                blank=True,
                max_length=300,
                null=True,
                upload_to="images/activity_attachment",
            ),
        ),
    ]
