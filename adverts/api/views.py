from datetime import datetime
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import  IsAuthenticated

from .permissions import IsAuthorOrReadOnly, IsNotAuthorOrReadOnly
from adverts.models import Advert, Order
from adverts.api.serializers import AdvertSerializer, OrderSerializer

now = datetime.now()
now = now.strftime("%Y-%m-%d")

class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all().order_by("-created_at")
    lookup_field = 'slug'
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

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
    permission_classes = [IsAuthenticated, IsNotAuthorOrReadOnly]

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

        advert.purchasers.add(request_user)
        advert.save()

        serializer.save(author=request_user, advert=advert)


class OrderRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        order_from = serializer.context['request'].data['order_from'] 
        order_from = datetime.strptime(order_from, "%Y-%m-%d").date()

        order_to = serializer.context['request'].data['order_to']
        order_to = datetime.strptime(order_to, "%Y-%m-%d").date()
        
        kwarg_id = self.kwargs['pk']

        q = Order.objects.get(id=kwarg_id)
        q = Advert.objects.get(id=q.advert_id)

        if order_from < q.available_from:
            raise ValidationError("You cannot order vehicle before available date")
        elif order_to > q.available_to:
            raise ValidationError("You cannot order vehicle after available date")
        elif order_from > order_to:
            raise ValidationError("Available to date must occur after available from date")

        instance = serializer.save()

    def perform_destroy(self, serializer):
        request_user = self.request.user
        kwarg_id = self.kwargs['pk']
        q = Order.objects.get(id=kwarg_id)

        advert = get_object_or_404(Advert, id=q.advert_id)

        advert.purchasers.remove(request_user)
        advert.save()