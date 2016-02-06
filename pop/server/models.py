from django.db import models
from django.conf import settings

# Create your models here.

class Case(models.Model):
    case_id = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    case_type = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, null=True)
    last_date = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "{}: {}".format(self.case_id, self.title)


class Party(models.Model):
    name = models.CharField(max_length=50, blank=True)
    party_type = models.CharField(max_length=50, blank=True)
    side = models.CharField(max_length=50, blank=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


class DocketEntry(models.Model):
    side = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    file = models.CharField(max_length=50, blank=True, null=True)
    case = models.ForeignKey('Case', on_delete=models.CASCADE)

