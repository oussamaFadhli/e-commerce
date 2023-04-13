from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from .models import CustomUser,Product, Order, AnounceAd, Review, Category, HeroAd


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise ValidationError("Price should be greater than zero")
        return value


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def get_product(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Product not found")

    def create(self, instance, validated_data):
        product_id = validated_data.pop('product_id', None)
        if product_id:
            product_id = self.get_product(product_id)
        else:
            raise serializers.ValidationError("Product ID is required")
        return instance

    def validate(self, attrs):
        user = self.context['request'].user
        if not user.is_authenticated:
            raise AuthenticationFailed("CustomUser not authenticated")
        return attrs


class AnounceAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnounceAd
        fields = '__all__'


class ReviewSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise ValidationError("Rating should be between 1 and 5")
        return value

    def get_product(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Product not found")

    def create(self, instance, validated_data):
        product_id = validated_data.pop('product_id', None)
        if product_id:
            product = self.get_product(product_id)
            # your create code here
        else:
            raise serializers.ValidationError("Product ID is required")
        return instance

    def validate(self, attrs):
        user = self.context['request'].user
        if not user.is_authenticated:
            raise AuthenticationFailed("CustomUser not authenticated")
        return attrs


class CategorySerilaizer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class HeroAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = HeroAd
        fields = '__all__'
