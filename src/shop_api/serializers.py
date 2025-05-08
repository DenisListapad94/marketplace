from rest_framework import serializers

from shop.models.product import ProductCategory, Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=30
    )
    price = serializers.FloatField()
    is_available = serializers.BooleanField(required=False)
    category = serializers.ChoiceField(
        choices=ProductCategory,
        default=ProductCategory.DEFAULT,
    )

    def create(self, validated_data):

        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'is_available', 'category']