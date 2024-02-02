from django.urls import path
from rest_framework_simplejwt import views

urlpatterns = [
    path('authentication/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]