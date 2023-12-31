# Generated by Django 4.2.3 on 2023-07-24 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("customer", "0001_initial"),
        ("meta", "0013_rename_city_id_yard_city"),
    ]

    operations = [
        migrations.CreateModel(
            name="Container_Attachment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Container",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("container_no", models.IntegerField()),
                ("submitter_initials", models.CharField(max_length=50)),
                ("comment", models.CharField(max_length=300)),
                ("location", models.CharField(max_length=50)),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("modified_datetime", models.DateTimeField(auto_now=True)),
                (
                    "container_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="meta.container_type",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
                (
                    "height",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="meta.container_height",
                    ),
                ),
                (
                    "length",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="meta.container_length",
                    ),
                ),
                (
                    "manufacture_year",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="meta.container_year",
                    ),
                ),
                (
                    "yard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="meta.yard"
                    ),
                ),
            ],
        ),
    ]
