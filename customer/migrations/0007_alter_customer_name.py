# Generated by Django 4.2.3 on 2023-07-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0006_alter_customer_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
