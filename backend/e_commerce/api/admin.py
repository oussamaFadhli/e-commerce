from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(CustomerServices)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Taxes)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(PaymentMethod)
admin.site.register(ShippingMethod)
admin.site.register(AnounceAd)
admin.site.register(HeroAd)
