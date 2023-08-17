"""
Problem: Valid Palindrome
Leetcode: https://leetcode.com/problems/valid-palindrome/
Solution: Two pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_palindrome(s: str) -> bool:
    """
    :param s: input string
    :return: True if string is a valid palindrome, False otherwise
    """

    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
