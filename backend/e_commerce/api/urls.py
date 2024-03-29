from django.urls import path
from .views import  LogoutView,LoginView,UserView,RegisterView,ProductList, ProductDetail, OrderList, OrderDetail, AnounceAdList,ReviewList,CategoryList,CategoryDetail,HeroAdList


urlpatterns = [
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserView.as_view(), name='user'),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('hero_ads/', HeroAdList.as_view()),
    path('anounce_ads/', AnounceAdList.as_view()),
    path('reviews/', ReviewList.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>',CategoryDetail.as_view()),
]
