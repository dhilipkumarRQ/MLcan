# Generated by Django 4.2.3 on 2023-07-29 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("container", "0011_alter_container_attachment_attachment_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="container_attachment",
            name="container",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="container_attachment",
                to="container.container",
            ),
        ),
    ]