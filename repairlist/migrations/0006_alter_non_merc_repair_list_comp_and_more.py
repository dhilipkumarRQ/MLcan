# Generated by Django 4.2.3 on 2023-07-29 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("meta", "0014_comp_component_dam_event_rep"),
        ("repairlist", "0005_merc_repair_list_combined_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="comp",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="meta.comp"
            ),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="component",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="meta.component",
            ),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="container_section",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="created_datetime",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="dam",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="meta.dam"
            ),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="damage_area",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="description",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="event",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="meta.event"
            ),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="hours",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="id_source",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="lgth_qty_area",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="lgth_qty_area2",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="location",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="material_cost",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="non_merc_repair_list",
            name="rep",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="meta.rep"
            ),
        ),
    ]
