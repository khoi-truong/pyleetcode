"""
Unit tests for valid anagram problem
"""

import unittest
from src.arrays_and_hashing.valid_anagram import is_anagram


class TestValidAnagram(unittest.TestCase):
    def test_valid_anagram(self):
        self.assertTrue(is_anagram("anagram", "nagaram"))
        self.assertFalse(is_anagram("rat", "car"))


if __name__ == "__main__":
    unittest.main()
