from django.test import TestCase
from .models import *

# Create your tests here.


class StoreTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Clothing")
        self.product = Product.objects.create(name="T-Shirt", price=20, category=self.category)

    def test_category_creation(self):
        category = Category.objects.create(name="Shoes")
        self.assertEqual(category.name, "Shoes")

    def test_product_creation(self):
        product = Product.objects.create(name="Jeans", price=50, category=self.category)
        self.assertEqual(product.name, "Jeans")
        self.assertEqual(product.price, 50)
        self.assertEqual(product.category, self.category)

    def test_product_category(self):
        product = Product.objects.get(name="T-Shirt")
        self.assertEqual(product.category.name, "Clothing")
