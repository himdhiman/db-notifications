from multiprocessing import context
from rest_framework import serializers
from core import models
from django.utils import timezone


class NotificationListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.NotificationList
        fields = ["id", "message", "read", "message_type", "created_at"]

    def create(self, validated_data):
        _ = validated_data.pop("user", None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class NotificationsSerializer(serializers.ModelSerializer):
    notifications = NotificationListSerializer(many=True)

    class Meta:
        model = models.Notification
        fields = ["notifications", "last_requested"]


class NotificationsSerializerWithoutNotification(serializers.ModelSerializer):

    class Meta:
        model = models.Notification
        fields = ["last_requested"]

    def to_representation(self, instance):
        primitive_repr =  super(NotificationsSerializerWithoutNotification, self).to_representation(instance)
        primitive_repr["notifications"] = []
        return primitive_repr
