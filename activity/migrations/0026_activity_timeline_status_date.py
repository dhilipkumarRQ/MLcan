# Generated by Django 4.2.3 on 2023-08-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("activity", "0025_alter_activity_timeline_activity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity_timeline",
            name="status_date",
            field=models.DateTimeField(null=True),
        ),
    ]
