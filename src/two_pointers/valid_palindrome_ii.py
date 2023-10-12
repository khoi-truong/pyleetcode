"""
Problem: Valid Palindrome II
Leetcode: https://leetcode.com/problems/valid-palindrome-ii/
"""

from abc import ABC, abstractmethod


class ValidPalindromeIISolution(ABC):
    @abstractmethod
    def valid_palindrome(self, s: str) -> bool:
        pass


class ValidPalindromeIITwoPointers(ValidPalindromeIISolution):
    """
    Solution: Two Pointers
    """

    def valid_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                s1 = s[left:right]
                s2 = s[left + 1 : right + 1]
                return self._is_palindrome(s1) or self._is_palindrome(s2)
            left += 1
            right -= 1
        return True

    def _is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
