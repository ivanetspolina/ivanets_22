import os

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


class ImageModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Nature")
        self.image = Image.objects.create(
            title="Sunset",
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            created_date=date.today(),
            age_limit=18
        )
        self.image.categories.add(self.category)
        self.image.save()

    def test_image_creation(self):
        self.assertEqual(self.image.title, "Sunset")

    def test_image_file(self):
        actual_file_name = os.path.basename(self.image.image.name)
        self.assertTrue(actual_file_name.startswith('test_image'))
        self.assertTrue(actual_file_name.endswith('.jpg'))

    def test_image_created_date(self):
        self.assertEqual(self.image.created_date, date.today())

    def test_image_age_limit(self):
        self.assertEqual(self.image.age_limit, 18)

    def test_image_category(self):
        self.assertIn(self.category, self.image.categories.all())

    def test_image_str(self):
        self.assertEqual(str(self.image), "Sunset")
