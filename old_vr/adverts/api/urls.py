from django.urls import include, path
from rest_framework.routers import DefaultRouter
from adverts.api import views as qv # adverts views


router = DefaultRouter()

router.register(r"adverts", qv.AdvertViewSet)

urlpatterns = [
    path("", include(router.urls)),


]