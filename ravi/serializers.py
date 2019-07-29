from rest_framework import serializers

from .models import Products,inventory


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'


class inventorySerializer(serializers.HyperlinkedModelSerializer):

    # product_name = ProductSerializer(read_only=True)
    # products = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all(), source='Products', write_only=True)
    products = ProductSerializer(read_only=True)
    class Meta:
        model = inventory
        fields = ('__all__')

        
