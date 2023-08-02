# Generated by Django 4.2.3 on 2023-07-24 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("activity", "0004_activity_inspection_attachment_activity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity_comment",
            name="activity",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="activity.activity_ledger",
            ),
        ),
        migrations.AddField(
            model_name="activity_comment",
            name="comment_text",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="activity_comment",
            name="comment_type",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="activity_comment",
            name="created_datetime",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="activity_comment",
            name="modified_datetime",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="activity_comment",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
