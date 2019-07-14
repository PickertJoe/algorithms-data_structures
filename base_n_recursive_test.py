# A program to test the functioning of the toStr function in the basen_recursive module

import unittest
from base_n_recursive import toStr


class BaseNTestCase(unittest.TestCase):
    """Ensures proper functioning of the toStr function"""

    def test_toStr(self):
        """Ensures that the appropriate string is returned from the toStr conversion using a base of 2"""
        test_string = '1010'
        test_int = 10
        self.assertEqual(test_string, toStr(test_int, 2))


unittest.main()
