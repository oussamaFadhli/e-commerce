from rest_framework import serializers
import re
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from .models import User, Product, Order, AnounceAd, Review, Category, HeroAd


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise ValidationError("Invalid email format")
        return value

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError("User not found")

    def update(self, instance, validated_data):
        user_id = validated_data.pop('id', None)
        if user_id:
            user_id = self.get_user(user_id)
        else:
            raise serializers.ValidationError("User ID is required")
        return instance

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed("Invalid username or password")
        return attrs


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
            raise AuthenticationFailed("User not authenticated")
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

    def create(self, instance,validated_data):
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
            raise AuthenticationFailed("User not authenticated")
        return attrs


class CategorySerilaizer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class HeroAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = HeroAd
        fields = '__all__'
