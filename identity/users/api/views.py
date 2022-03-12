from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope, OAuth2Authentication
)

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer
from .permissions import IsAdmin, IsOwnerOrAdminOrStaff
from rest_framework.filters import OrderingFilter, SearchFilter


class UserDetails(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsOwnerOrAdminOrStaff, TokenHasReadWriteScope]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UsersList(generics.ListAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope, IsAdmin]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # filter classes
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter, )
    # filter, search, ordering parameters
    search_fields = ['email', 'first_name', 'last_name']
    filter_fields = ['email', 'first_name', 'last_name', 'is_active']
    ordering_fields = ['email', 'first_name', 'last_name', 'is_active']


class UserFromToken(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]

    def get(self, request):
        try:
            user = get_user_model().objects.get(pk=request.user.pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response(data=None, status=status.HTTP_404_NOT_FOUND)
