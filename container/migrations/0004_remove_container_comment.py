# Generated by Django 4.2.3 on 2023-07-25 07:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("container", "0003_container_attachment_attachment_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="container",
            name="comment",
        ),
    ]