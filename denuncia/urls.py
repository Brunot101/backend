from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('denuncia/add', views.DenunciaCreateView.as_view(), name='denuncia-create-view'),
    path('denuncia/', views.DenunciaListView.as_view(), name='denuncia-list-view'),
    path('denuncia/<int:pk>/', views.DenunciaRetrieveView.as_view(), name='denuncia-detail-view'),
]

urlpatterns += staticfiles_urlpatterns()