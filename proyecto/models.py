from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()  # Edad en años, usa PositiveIntegerField para valores positivos
    descripcion = models.TextField()  # Descripción más extensa
    especie = models.CharField(max_length=100)  # Por ejemplo, "Perro", "Gato"
    raza = models.CharField(max_length=100)  # Por ejemplo, "Labrador", "Siamés"
    color = models.CharField(max_length=50)  # Por ejemplo, "Blanco", "Negro"
    registroveterinario = models.FileField(upload_to='veterinario/', null=True, blank=True)  # Información sobre el historial médico
    adoptado = models.BooleanField(default=False)  # Indica si la mascota ha sido adoptada
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro
    def __str__(self):
        return self.nombre
