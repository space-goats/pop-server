from server.models import *
from rest_framework.serializers import ModelSerializer


class CaseSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = ('id', 'case_id')
