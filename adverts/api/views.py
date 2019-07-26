from rest_framework import viewsets

from .permissions import IsAuthorOrReadOnly
from adverts.models import Advert, Order
from adverts.api.serializers import AdvertSerializer, OrderSerializer

class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all().order_by("available_from")
    # lookup_field = 'slug'
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)