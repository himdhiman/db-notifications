from django.db import models
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save


class NotificationList(models.Model):
    message_type_choices = (("N", "Notify"), ("W", "Warning"))
    message = models.TextField(blank=True, null=True)
    message_type = models.CharField(choices=message_type_choices, max_length=20)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=True)

    def __str__(self):
        return str(self.id)


class Notification(models.Model):
    user = models.EmailField(verbose_name="email", unique=True, max_length=60)
    username = models.CharField(unique=True, max_length=20)
    notifications = models.ManyToManyField(NotificationList, null=True, blank=True)
    last_requested = models.DateTimeField(default=now, editable=True)

    def __str__(self):
        return self.user


@receiver(post_save, sender=Notification)
def after_creating_user(sender, instance, created, **kwargs):
    if not created:
        return
    message = f"Hello {instance.username}, Welcome to DirtyBits."
    obj = NotificationList.objects.create(message=message, message_type="N")
    instance.notifications.add(obj)
    instance.save()
    return
