from django.contrib.auth.models import User
from django.db import models


class Docente(User):
    legajo = models.PositiveIntegerField()
