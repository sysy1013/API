from rest_framework import serializers
from .models import Trade_information

class TradeinformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trade_information
        fields = ('bankname','account_number','to_name','from_name','created_at','updated_at')