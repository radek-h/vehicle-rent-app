from datetime import datetime
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .permissions import IsAuthorOrReadOnly
from adverts.models import Advert, Order
from adverts.api.serializers import AdvertSerializer, OrderSerializer

now = datetime.now()
now = now.strftime("%Y-%m-%d")

class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.filter(available_to__gte=now)
    lookup_field = 'slug'
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Order.objects.filter(advert__slug=kwarg_slug)



class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order_from = serializer.context['request'].data['order_from']       
        order_from = datetime.strptime(order_from, "%Y-%m-%d").date()

        order_to = serializer.context['request'].data['order_to']
        order_to = datetime.strptime(order_to, "%Y-%m-%d").date()

        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        advert = get_object_or_404(Advert, slug=kwarg_slug)
        query = Advert.objects.get(slug=kwarg_slug)

        if advert.orders.filter(author=request_user).exists():
            raise ValidationError("You have already order this vehicle earlier!")
        elif query.author == request_user:
            raise ValidationError("You cannot order your own vehicle!")
        elif order_from < query.available_from:
            raise ValidationError("You cannot order vehicle before available date")
        elif order_to > query.available_to:
            raise ValidationError("You cannot order vehicle after available date")

        serializer.save(author=request_user, advert=advert)
