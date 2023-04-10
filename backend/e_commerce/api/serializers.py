from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from .models import CustomUser, Product, Order, AnounceAd, Review, Category, HeroAd

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=128, min_length=8)
    confirm_password = serializers.CharField(write_only=True, max_length=128, min_length=8)
    token = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'confirm_password', 'first_name', 'last_name', 'address', 'country', 'city', 'state', 'zip_code', 'phone_number', 'token')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': True},
            'username': {'required': True},
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            'phone_number': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        password = validated_data.get('password')
        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            country=validated_data['country'],
            city=validated_data['city'],
            state=validated_data['state'],
            zip_code=validated_data['zip_code'],
            phone_number=validated_data['phone_number']
        )
        if password:
            user.password = make_password(password)
        user.save()
        print(validated_data)
        return user

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)

        return token



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
