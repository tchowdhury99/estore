from django.test import TestCase
from .models import Category

class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create()
        self.category.title = "Hello"
        self.category.slug = "hello"
        self.category.save()
    def testTitle(self):
        expected_string = "Hello"
        self.assertEqual(self.category.__str__(), expected_string, "Title is not same as initialized.")
