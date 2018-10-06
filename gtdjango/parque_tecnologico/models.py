from django.db import models

DEFAULT_MAX_LENGTH = 100


class Recurso(models.Model):
    nombre = models.PositiveIntegerField(
        unique=True
    )

    tipo_recurso = models.ForeignKey(
        'TipoRecurso',
        on_delete=models.CASCADE
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True

    )

    ultima_actualizacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        if self.tipo_recurso.indetificador == "PM":
            return "{0!s}-{1!s}".format(self.nombre, self.tipo_recurso.indetificador)
        else:
            return "{0!s}-{1!s}".format(self.tipo_recurso.indetificador, self.nombre)


class TipoRecurso(models.Model):
    nombre = models.CharField(
        max_length=DEFAULT_MAX_LENGTH
    )
    indetificador = models.CharField(
        max_length=10
    )

    def __str__(self):
        return self.nombre
