from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from classnowapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clases', views.ClasesView, basename='clase')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.userCreateView.as_view()),
    path('user/<int:pk>/', views.userDetailView.as_view())
]

urlpatterns += router.urls