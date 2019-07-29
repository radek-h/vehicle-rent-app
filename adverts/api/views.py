import datetime
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsAuthorOrReadOnly
from adverts.models import Advert, Order
from adverts.api.serializers import AdvertSerializer, OrderSerializer

now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d")

class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.filter(available_to__gte=now)
    lookup_field = 'slug'
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# class AdvertListAPIView(generics.ListCreateAPIView):
#     queryset = Advert.objects.all().order_by("available_from")
#     serializer_class = AdvertSerializer
#     permission_classes = [IsAuthorOrReadOnly]