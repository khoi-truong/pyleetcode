"""
Problem: Valid Palindrome II
"""

import unittest
from src.two_pointers.valid_palindrome_ii import (
    ValidPalindromeIISolution,
    ValidPalindromeIITwoPointers,
)


class TestValidPalindromeII(unittest.TestCase):
    """
    Test cases for valid palindrome II problem
    """

    def test_valid_palindrome(self):
        sut = ValidPalindromeIITwoPointers()
        self._test_solution(sut)

    def _test_solution(self, sut: ValidPalindromeIISolution):
        self.assertTrue(sut.valid_palindrome("aba"))
        self.assertTrue(sut.valid_palindrome("abca"))
        self.assertTrue(sut.valid_palindrome("abcca"))
        self.assertFalse(sut.valid_palindrome("abc"))
        self.assertFalse(sut.valid_palindrome("abcda"))
        self.assertTrue(sut.valid_palindrome("abcca"))
        self.assertFalse(sut.valid_palindrome("abccda"))
