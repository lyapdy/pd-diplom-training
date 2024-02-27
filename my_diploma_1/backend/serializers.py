from rest_framework import serializers

from backend.models import Shop, Product


class ShopSerializer(serializers.ModelSerializer):
    #address = serializers.CharField(max_length=100 )
    class Meta:
        model = Shop
        fields = ('id', 'name', 'state')
                  #'address'


class ProductSerializer(serializers.ModelSerializer):
    #shop = serializers.StringRelatedField()
    shop = ShopSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'quantity', 'price', 'shop')
