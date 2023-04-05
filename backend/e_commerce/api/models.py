from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    ROLES = [
        ('US', 'User'),
        ('SF', 'STAFF'),
        ('CS', 'CUSTOMER_SERVICE'),
        ('SU', 'SUPER_USER'),
    ]
    user_roles = models.CharField(
        max_length=2,
        choices=ROLES,
        default='US',
    )
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username},{self.user_roles}"


class CustomerServices(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_date = models.DateField(auto_now=True)
    report_subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"{self.user},{self.report_subject},{self.report_date}"


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=255)
    stock_quantity = models.IntegerField()
    date_added = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id},{self.category},{self.product_name}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    date_added = models.DateTimeField()

    def __str__(self):
        return f"{self.product},{self.rating},{self.date_added}"


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=255)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
    usage_limit = models.IntegerField()

    def __str__(self):
        return self.coupon_code


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    STATUS = [
        ('OPC', 'ORDER_PLACED_BY_CLIENT'),
        ('OV', 'ORDER_VALIDATED'),
        ('OT', 'ORDER_TRANSFERD'),
        ('OHC', 'ORDER_HANDED_OVER_TO_CARRIER'),
        ('LV', 'LIVERED'),
        ('OC', 'ORDER_CANCELED'),
    ]
    order_status = models.CharField(
        max_length=30,
        choices=STATUS,
    )
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    shipping_method = models.ForeignKey(
        'ShippingMethod', on_delete=models.CASCADE)
    payment_method = models.ForeignKey(
        'PaymentMethod', on_delete=models.CASCADE)
    discount = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.id},{self.user},{self.order_status},{self.subtotal}"


class PaymentMethod(models.Model):
    payment_method_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.payment_method_name


class ShippingMethod(models.Model):
    shipping_method_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.shipping_method_name
