from server.models import *
from rest_framework.serializers import ModelSerializer


class CaseSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = ('id', 'case_id', 'title', 
                  'case_type', 'status', 'last_date', 'party', 'docketentry')
        depth = 1


class PartySerializer(ModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'name', 'party_type', 'side')

class DocketEntrySerializer(ModelSerializer):
    class Meta:
        model = DocketEntry
        fields = ('id', 'side', 'date', 'name', 'file')


