from django.conf import settings
from adverts.api import views as av # adverts views
from django.urls import include, path
from django.conf.urls.static import static
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


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)