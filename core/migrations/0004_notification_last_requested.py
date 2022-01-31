# Generated by Django 3.2.11 on 2022-01-31 12:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_rename_notification_list_notificationlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="last_requested",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
