from rest_framework import generics
from .models import User, Product, Order, AnounceAd, Review, Category, HeroAd
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, AnounceAdSerializer, ReviewSerlizer, CategorySerilaizer, HeroAdSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AnounceAdList(generics.ListAPIView):
    queryset = AnounceAd.objects.order_by('-id')[:1]
    serializer_class = AnounceAdSerializer

class HeroAdList(generics.ListAPIView):
    queryset = HeroAd.objects.order_by('-id')[:5]
    serializer_class = HeroAdSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerlizer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilaizer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilaizer


