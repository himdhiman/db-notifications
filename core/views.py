from rest_framework.views import APIView
from core import serializers, models, middleware
from rest_framework import status
from rest_framework.response import Response


class CreateUserNotification(APIView):
    def post(self, request):
        request_data = request.data
        models.Notification.objects.create(
            user=request_data["user"], username=request_data["username"]
        )
        return Response(status=status.HTTP_201_CREATED)


class DeleteUserNotification(APIView):
    def post(self, request):
        request_data = request.data
        models.Notification.objects.filter(user=request_data["user"]).delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class AddNotification(APIView):
    def post(self, request):
        request_data = request.data
        user = request_data.pop("user", None)
        obj = serializers.NotificationListSerializer(data=request_data)
        if obj.is_valid():
            obj = obj.save()
            not_obj = models.Notification.objects.filter(user=user)
            if len(not_obj) == 0:
                not_obj = models.Notification(user=user)
                not_obj.save()
            else:
                not_obj = not_obj.first()
            not_obj.notifications.add(obj)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GetNotifications(APIView):
    def get(self, request):
        access_token = request.headers["Authorization"].split(" ")[1]
        response = middleware.Authentication.isAuthenticated(access_token)
        if not response["success"]:
            data = {"success": False, "message": "Unauthorized Request !"}
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
        user = response["data"]["email"]
        notifications = models.Notification.objects.get(user=user)
        data = serializers.NotificationsSerializer(notifications)
        return Response(data=data.data, status=status.HTTP_200_OK)
