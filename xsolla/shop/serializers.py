from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['article', 'name', 'type', 'price', 'count']

