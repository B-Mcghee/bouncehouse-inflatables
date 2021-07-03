from rest_framework import serializers
from .models import Collection, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price_per_day",
            "get_image",
            "get_thumbnail"
        )


class CollectionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Collection
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )

