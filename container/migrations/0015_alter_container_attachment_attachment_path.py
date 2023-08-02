# Generated by Django 4.2.3 on 2023-07-31 03:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("container", "0014_container_attachment_attachment_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="container_attachment",
            name="attachment_path",
            field=models.ImageField(
                blank=True,
                max_length=200,
                null=True,
                upload_to="images/container/%y/%m/%d",
            ),
        ),
    ]
