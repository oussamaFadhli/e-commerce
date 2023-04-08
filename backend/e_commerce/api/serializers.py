from rest_framework import serializers
from .models import User, Product, Order, Ad,Review,Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

class ReviewSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class CategorySerilaizer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
