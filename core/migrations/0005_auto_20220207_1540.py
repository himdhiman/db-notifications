# Generated by Django 3.2.11 on 2022-02-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_notification_last_requested"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="username",
            field=models.CharField(default="xyz", max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="notification",
            name="notifications",
            field=models.ManyToManyField(
                blank=True, null=True, to="core.NotificationList"
            ),
        ),
    ]
