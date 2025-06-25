from django.db import models

class Contacto(models.Model):
    TIPO_MENSAJE = [
        ('Sugerencia', 'Sugerencia'),
        ('Reclamo', 'Reclamo'),
        ('Felicitacion', 'Felicitacion'),
    ]
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo = models.CharField(max_length=20, choices=TIPO_MENSAJE)
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"
