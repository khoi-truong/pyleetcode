"""
Problem: Valid Anagram
Leetcode: https://leetcode.com/problems/valid-anagram/
Solution: Hashing
Time Complexity: O(n)
Space Complexity: O(1)
"""


def is_anagram(s: str, t: str) -> bool:
    """
    :param s: input string
    :param t: input string
    :return: True if s is an anagram of t, False otherwise
    """
    frequencies = dict[str, int]()
    for ch in s:
        frequencies[ch] = frequencies.get(ch, 0) + 1
    for ch in t:
        if ch not in frequencies:
            return False
        frequencies[ch] -= 1
    for frequency in frequencies.values():
        if frequency != 0:
            return False
    return True
