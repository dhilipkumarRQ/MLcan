# Generated by Django 4.2.3 on 2023-08-02 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("container", "0015_alter_container_attachment_attachment_path"),
        ("activity", "0013_remove_activity_ledger_created_datetime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity_ledger",
            name="activity_type",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="activity_ledger",
            name="container",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="container.container"
            ),
        ),
    ]
