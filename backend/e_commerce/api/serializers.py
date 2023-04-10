from rest_framework import serializers
import re
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError,AuthenticationFailed
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
            user = self.get_user(user_id)
            # your update code here
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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AnounceAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnounceAd
        fields = '__all__'


class ReviewSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class CategorySerilaizer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class HeroAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = HeroAd
        fields = '__all__'
