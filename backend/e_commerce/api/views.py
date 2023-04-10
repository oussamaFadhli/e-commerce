from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Product, Order, AnounceAd, Review, Category, HeroAd
from .serializers import  CustomUserSerializer,ProductSerializer, OrderSerializer, AnounceAdSerializer, ReviewSerlizer, CategorySerilaizer, HeroAdSerializer



class RegisterView(APIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
    authentication_classes = [JSONWebTokenAuthentication]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



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
