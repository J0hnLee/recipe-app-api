"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add(self):
        """Test the add function"""
        
        self.assertEqual(calc.add(3, 2), 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0.0001, 0), 0.0001)


