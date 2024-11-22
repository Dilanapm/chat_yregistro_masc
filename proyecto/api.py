from rest_framework import viewsets, permissions
from .models import Mascota
from .serializers import MascotaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    permission_classes = [permissions.AllowAny] # con este permiso vamos a pasar sin necesidad de autenticacion
    serializer_class = MascotaSerializer
    @action(detail=True, methods=['post'])
    def adoptado(self, request, pk=None):
        mascota = self.get_object()
        mascota.adoptado = not mascota.adoptado
        mascota.save()
        return Response({'status': 'mascota adoptada' if mascota.adoptado else 'mascota no adoptada'
                         },status=status.HTTP_200_OK)