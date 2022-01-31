from rest_framework import serializers
from core import models
from django.utils import timezone


class NotificationListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.NotificationList
        fields = "__all__"

    def create(self, validated_data):
        _ = validated_data.pop("user", None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance



class NotificationsSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    notifications = NotificationListSerializer(many=True)

    class Meta:
        model = models.Notification
        fields = "__all__"

    def to_representation(self, instance):
        primitive_repr = super(NotificationsSerializer, self).to_representation(instance)
        instance.last_requested = timezone.now()
        instance.save()
        # print(primitive_repr)
        return primitive_repr





