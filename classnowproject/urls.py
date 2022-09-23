from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from classnowapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clases', views.ClasesView, basename='clase') # Para enviar tareas se escribe /clases/ y la información en formato JSON.
# Para hacer put, get y delete debo especificar el id de la tarea que se quiere afectar Ejemplo:/clases/2
 
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()), # Metodo POST con Username y Password --> Me devuelve tokens.
    path('refresh/', TokenRefreshView.as_view()), # Metodo POST con el token refresh en JSON --> Me devuelve un token access.
    path('user/', views.userCreateView.as_view()), # Metodo POST para crear un usuario. Se necesita datos en JSON. --> Me devuelve Token access y token refresh.
    path('user/<int:pk>/', views.userDetailView.as_view()) # Metodo GET para visualizar datos de un usuario. Se necesita id del usuario y access token en auth/bearer token.
]

urlpatterns += router.urls