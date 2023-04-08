from django.urls import path
from .views import UserList, UserDetail, ProductList, ProductDetail, OrderList, OrderDetail, AdList,ReviewList,CategoryList,CategoryDetail


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('ads/', AdList.as_view()),
    path('reviews/', ReviewList.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>',CategoryDetail.as_view())
]
