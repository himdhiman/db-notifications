from django.db import models
from django.utils.timezone import now


class Notification_List(models.Model):
    message_type_choices = (("N", "Notify"), ("W", "Warning"))
    message = models.TextField(blank=True, null=True)
    message_type = models.CharField(choices=message_type_choices, max_length=20)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=True)


class Notification(models.Model):
    user = models.EmailField(verbose_name="email", unique=True, max_length=60)
    notifications = models.ManyToManyField(Notification_List)
