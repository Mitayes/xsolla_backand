from django.http import Http404
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from shop.serializers import ProductSerializer
from shop.models import Product
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet that for listing or retrieving products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['article', 'type', 'price']
    # При необходимости можно добавить требование авторизации для работы с api, раскомментировав permission_classes
    # permission_classes = [permissions.IsAuthenticated]

    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         self.perform_destroy(instance)
    #     except Http404:
    #         pass
    #     return Response(status=status.HTTP_204_NO_CONTENT)
