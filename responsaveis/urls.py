from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('responsavel/create', views.ResponsavelProfileCreateView.as_view(), name='responsavel-profile-create-view'),
    path('responsavel/associate/<int:aluno_id>/', views.AssociateDependenteView.as_view(), name='responsavel-associate-dependente-view'),
]

urlpatterns += staticfiles_urlpatterns()