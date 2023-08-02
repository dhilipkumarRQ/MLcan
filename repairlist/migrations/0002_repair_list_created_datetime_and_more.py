# Generated by Django 4.2.3 on 2023-07-24 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("meta", "0013_rename_city_id_yard_city"),
        ("repairlist", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="repair_list",
            name="created_datetime",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="repair_list",
            name="damaged_area",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="meta.damage_area",
            ),
        ),
        migrations.AddField(
            model_name="repair_list",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="repair_list",
            name="modified_datetime",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="repair_list",
            name="repair_area",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="meta.repair_area",
            ),
        ),
        migrations.AddField(
            model_name="repair_list",
            name="repair_code",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="repair_list",
            name="repair_component",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="repairlist.non_merc_repair_list",
            ),
        ),
        migrations.AddField(
            model_name="repair_list",
            name="repair_component_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="meta.container_type",
            ),
        ),
        migrations.AddField(
            model_name="repair_list",
            name="repair_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="meta.repair_type",
            ),
        ),
        migrations.AddField(
            model_name="repair_list",
            name="version",
            field=models.IntegerField(null=True),
        ),
    ]
