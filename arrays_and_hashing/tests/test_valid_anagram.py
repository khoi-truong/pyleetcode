"""
Problem: Valid Anagram
"""

import unittest
from arrays_and_hashing.valid_anagram import is_anagram


class TestValidAnagram(unittest.TestCase):
    """
    Test cases for valid anagram problem
    """

    def test_valid_anagram(self):
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("a", "b"))
        self.assertTrue(is_anagram("a", "a"))
        self.assertFalse(is_anagram("rat", "car"))
        self.assertTrue(is_anagram("anagram", "nagaram"))


if __name__ == "__main__":
    unittest.main()
