from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('notifications/<int:pk>/', views.UserNotificationListView.as_view(), name='user-notification-list-view'),
    path('notifications/edit/<int:pk>/', views.UserNotificationUpdateView.as_view(), name='user-notification-update-view'),
]

urlpatterns += staticfiles_urlpatterns()