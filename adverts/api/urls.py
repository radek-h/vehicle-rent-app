from django.conf import settings
from adverts.api import views as av # adverts views
from django.urls import include, path, re_path
from core.views import IndexTemplateView
from rest_framework.routers import DefaultRouter



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

      path("order/<int:pk>/",
         av.OrderRUDAPIView.as_view(),
         name='orders-detail'),

      re_path(r"^.*$", IndexTemplateView.as_view(), name='entry-point')
]