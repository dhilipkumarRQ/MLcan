# Generated by Django 4.2.3 on 2023-07-24 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("meta", "0007_quantity"),
    ]

    operations = [
        migrations.CreateModel(
            name="Yard",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=10)),
                ("pincode", models.IntegerField()),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("modified_datetime", models.DateTimeField(auto_now=True)),
                (
                    "City",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="meta.city",
                    ),
                ),
                (
                    "province",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="meta.province",
                    ),
                ),
            ],
        ),
    ]
