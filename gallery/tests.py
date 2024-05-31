from django.test import TestCase
from gallery.models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date


class CategoryTest(TestCase):
    def test_category_creation1(self):
        category = Category.objects.create(name="Nature")
        self.assertEqual(category.name, "Nature")

    def test_category_creation2(self):
        category = Category.objects.create(name="Nature")
        self.assertEqual(str(category), "Nature")
