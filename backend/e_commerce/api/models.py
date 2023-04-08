from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"


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
    image_url = models.ImageField(upload_to='products_photo/')
    stock_quantity = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)
    date_added = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id},{self.category},{self.product_name}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
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


class ShippingMethod(models.Model):
    SHIPPING = [
        ('ST', 'STANDARD'),
        ('PR', 'PREMIUM'),
    ]
    shipping_method_name = models.CharField(
        max_length=30,
        choices=SHIPPING,
        default='ST',
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.shipping_method_name


class Taxes(models.Model):
    tax = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.tax)


class PaymentMethod(models.Model):
    PAYEMENT = [
        ('CH', 'CASH'),
        ('MC', 'MASTERCARD'),
        ('VS', 'VISA'),
        ('D17', 'D17'),
    ]
    payment_method_name = models.CharField(
        max_length=15,
        choices=PAYEMENT,
        default='CH',
    )
    description = models.TextField()

    def __str__(self):
        return self.payment_method_name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)], default=1)
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
    shipping_method = models.ForeignKey(
        ShippingMethod, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.CASCADE)
    tax = models.ForeignKey(
        Taxes, on_delete=models.CASCADE)
    discount = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def calculate_subtotal(self):
        return ((Decimal(self.quantity) * self.product.price)+(self.tax.tax)*self.quantity)-self.discount.discount_amount

    def save(self, *args, **kwargs):
        self.product.stock_quantity -= self.quantity
        self.product.save()

        self.subtotal = self.calculate_subtotal()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id},{self.user},{self.order_status},{self.subtotal}"



class Ad(models.Model):
    title_hero = models.CharField(max_length=200)
    title_anounce = models.CharField(max_length=200)
    image_hero = models.ImageField(upload_to='ads/')
    image_anounce = models.ImageField(upload_to='ads/')
    url_hero = models.URLField(max_length=200)
    url_anounce = models.URLField(max_length=200)
    start_date_hero = models.DateTimeField()
    start_date_anounce = models.DateTimeField()
    end_date_hero = models.DateTimeField()
    end_date_anounce = models.DateTimeField()


    def __str__(self):
        return f"{self.title_hero},{self.title_anounce}"
