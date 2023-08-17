"""
Problem: Valid Palindrome
"""

import unittest
from two_pointers.valid_palindrome import is_palindrome


class TestValidPalindrome(unittest.TestCase):
    """
    Test cases for valid palindrome problem
    """

    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("abc"))

    def test_valid_palindrome_with_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_valid_palindrome_with_one_char(self):
        self.assertTrue(is_palindrome("a"))


if __name__ == "__main__":
    unittest.main()
