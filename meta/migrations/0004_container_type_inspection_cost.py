# Generated by Django 4.2.3 on 2023-07-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meta", "0003_container_height_container_length_container_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="container_type",
            name="inspection_cost",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
