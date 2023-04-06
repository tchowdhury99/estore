from django.test import TestCase
from products.models import Product
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


    def test_str2(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")
    
    def test_str3(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")
    def test_str4(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")
    
    def test_str5(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")

    def test_str6(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")

    def test_str7(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")

    def test_str8(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")

    def test_str9(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")

    def test_str10(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")

    def test_str11(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")

    def test_str12(self):
        expected_string = "Hi v1"
        self.assertEqual(self.product.__str__(), expected_string, "Product name is not same as initialized")
