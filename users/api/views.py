from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer

from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all().order_by("username")
    serializer_class = UserDisplaySerializer
    permission_classes = [IsAuthenticated]


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        instance = get_object_or_404(CustomUser, id=pk)
        serializer = UserDisplaySerializer(instance)
        return Response(serializer.data)
