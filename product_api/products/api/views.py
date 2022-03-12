from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView
)

from products.models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from .permissions import IsAdmin


class Create(CreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope, IsAdmin]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Update(UpdateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope, IsAdmin]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class Delete(DestroyAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope, IsAdmin]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class Retrieve(RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    queryset = Product.objects.all()
    lookup_field = 'slug'
    serializer_class = ProductDetailSerializer


class List(ListAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = ProductSerializer

    def get_queryset(self):
        request = self.request
        if request.user.is_superuser or request.user.is_staff:
            return Product.objects.all()
        return Product.objects.all().filter(is_active=True)
