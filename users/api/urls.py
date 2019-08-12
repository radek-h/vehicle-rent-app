from django.urls import path
from users.api.views import UserListAPIView, UserAPIView

urlpatterns = [
    path("users/", UserListAPIView.as_view(), name='user-list'),
    path("user/<int:pk>/", UserAPIView.as_view(), name='user'),
]