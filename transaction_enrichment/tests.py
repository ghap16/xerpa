from django.core.exceptions import ValidationError
from django.test import TestCase

from .validators import valid_image_extension, validate_not_zero


class EnrichmentTestCase(TestCase):
    def setUp(self):
        self.valid_image = (
            "https://media.wired.com/photos/Uber_Logobit_Digital_black.jpg"
        )
        self.invalid_image = (
            "https://media.wired.com/photos/Uber_Logobit_Digital_black.html"
        )

    def test_valid_image_extension(self):
        self.assertEqual(valid_image_extension(self.valid_image), None)

    def test_invalid_image_extension(self):
        with self.assertRaises(ValidationError):
            valid_image_extension(self.invalid_image)

    def test_validate_not_zero(self):
        self.assertEqual(validate_not_zero(1), None)
        self.assertEqual(validate_not_zero(-1), None)

    def test_validate_is_zero(self):
        with self.assertRaises(ValidationError):
            validate_not_zero(0)
