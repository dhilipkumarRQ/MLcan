# Generated by Django 4.2.3 on 2023-08-02 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("meta", "0014_comp_component_dam_event_rep"),
        ("activity", "0017_remove_activity_quote_repair_list_repair_type_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="activity_quote_repair_list",
            name="repair_list",
        ),
        migrations.RemoveField(
            model_name="activity_quote_repair_list",
            name="repair_object_id",
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