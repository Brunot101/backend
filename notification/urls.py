from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('notifications/', views.UserNotificationListAPIView.as_view(), name='user-notification-list-view'),
    
]

urlpatterns += staticfiles_urlpatterns()