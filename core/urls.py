from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("add/", views.AddNotification.as_view()),
    path("get/", views.GetNotifications.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
