from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('denuncia/', views.DenunciaCreateListView.as_view(), name='denuncia-create-list-view'),
    path('denuncia/<int:pk>/', views.DenunciaRetrieveView.as_view(), name='denuncia-detail-view'),
]

urlpatterns += staticfiles_urlpatterns()