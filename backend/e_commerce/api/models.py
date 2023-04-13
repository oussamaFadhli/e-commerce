from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from decimal import Decimal
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=40,blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
class CustomerServices(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_subtotal(self):
        return ((Decimal(self.quantity) * self.product.price)+(self.tax.tax)*self.quantity)-self.discount.discount_amount+self.shipping_method.price

    def save(self, *args, **kwargs):
        self.product.stock_quantity -= self.quantity
        self.product.save()

        self.subtotal = self.calculate_subtotal()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id},{self.user},{self.order_status},{self.subtotal}"


class AnounceAd(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='anounce_ads/')
    url = models.URLField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"

class HeroAd(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_ad/')
    url = models.URLField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

