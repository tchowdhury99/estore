from django.test import TestCase
from .models import Product
from categories.models import Category
from datetime import datetime

class ProductTest(TestCase):
    def setUp(self):
        self.category = Category()
        self.category.title = "Hello"
        self.category.save()

        self.product = Product()
        self.product.title = "Hi v1"
        self.product.category = self.category
        self.product.published_at = "2022-05-01 09:30:04.550661"
        self.product.description = "Hi v1 is a device to say hi"
        self.product.price = "100000"
        self.product.quantity = 2
        self.product.save()


    def test_str(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")

    