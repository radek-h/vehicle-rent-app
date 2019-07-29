from django.urls import include, path
from rest_framework.routers import DefaultRouter
from adverts.api import views as av # adverts views


router = DefaultRouter()

router.register(r"adverts", av.AdvertViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path('adverts/<slug:slug>/orders/',
         av.OrderListAPIView.as_view(),
         name='orders-list'),

    path('adverts/<slug:slug>/order/',
         av.OrderCreateAPIView.as_view(),
         name='order-create'),


]