from django.test import TestCase
from ..utils import validate_ean

class UtilsTestCase(TestCase):
    def test_validate_ean(self):
        self.assertTrue(validate_ean('9780201310054'))
        self.assertFalse(validate_ean('9780201310055'))
        with self.assertRaises(ValueError):
            validate_ean('978020131005')