# Generated by Django 4.2.3 on 2023-08-02 10:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("activity", "0019_rename_activity_activity_quote_repair_list_re"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity_quote_repair_list",
            name="comment",
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]