from rest_framework import serializers
from .models import Mascota
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('id','nombre','edad','descripcion','especie','raza','color','registroveterinario','adoptado','created_at')
        read_only_fields = ('id','created_at')