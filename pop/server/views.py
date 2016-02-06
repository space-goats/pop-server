from django.shortcuts import render
from server.models import *
from server.serializers import *

from rest_framework import viewsets

# Create your views here.


class CaseList(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
