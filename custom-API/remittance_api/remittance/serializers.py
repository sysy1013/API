from rest_framework import serializers
from .models import Trade

class TradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trade
        fields = ('category','created_at','updated_at')
