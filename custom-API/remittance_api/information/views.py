from rest_framework import generics, mixins
from .serializers import TradeinformationSerializer
from .models import Trade_information

class TradeinformationListAPI(generics.ListAPIView,mixins.ListModelMixin):
    queryset = Trade_information.objects.all()
    serializer_class = TradeinformationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
