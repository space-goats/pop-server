from django.db import models
from django.conf import settings

# Create your models here.

class Case(models.Model):
    case_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "{}: {}".format(case_id)

