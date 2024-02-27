from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('responsavel/create', views.ResponsavelProfileCreateView.as_view(), name='responsavel-profile-create-view'),
]

urlpatterns += staticfiles_urlpatterns()