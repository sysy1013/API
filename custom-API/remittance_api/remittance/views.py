from rest_framework import generics, mixins
from .serializers import TradeSerializer
from .models import Trade


class TradeListAPI(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

