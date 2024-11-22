from rest_framework import routers
from .api import MascotaViewSet
from django.urls import path, include
from . import chatview  # Importar tu archivo de vistas del chatbot

# Crear un enrutador para las vistas basadas en ViewSets
router = routers.DefaultRouter()
router.register('api/mascotas', MascotaViewSet, 'mascota')

# Definir las rutas manuales
urlpatterns = [
    path('api/chatbot/', chatview.chatbot_response, name='chatbot_response'),
    path('', include(router.urls)),  # Incluir las rutas del enrutador
]
