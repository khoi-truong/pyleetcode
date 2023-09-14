"""
Problem: Minimum Window Substring
Leetcode: https://leetcode.com/problems/minimum-window-substring/
"""

from abc import ABC, abstractmethod


class Solution(ABC):
    @abstractmethod
    def min_window(self, s: str, t: str) -> str:
        pass


class SlidingWindowSolution(Solution):
    """
    Solution: Sliding Window
    Time complexity: O(n + m)
    Space complexity: O(n + m)
    """

    def min_window(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        s_len = len(s)
        min_length = s_len + 1
        substring_start = 0

        required_freq = dict[str, int]()
        for char in t:
            required_freq[char] = required_freq.get(char, 0) + 1
        required_matches = len(required_freq)

        window_freq = dict[str, int]()
        for char in required_freq:
            window_freq[char] = 0
        window_matches = 0

        start = 0
        for end in range(s_len):
            right_char = s[end]
            if required_freq.get(right_char):
                window_freq[right_char] += 1
                if window_freq[right_char] == required_freq[right_char]:
                    window_matches += 1
            while window_matches == required_matches:
                if end - start + 1 < min_length:
                    min_length = end - start + 1
                    substring_start = start
                left_char = s[start]
                if left_char in required_freq:
                    window_freq[left_char] -= 1
                    if window_freq[left_char] < required_freq[left_char]:
                        window_matches -= 1
                start += 1

        if min_length > s_len:
            return ""
        return s[substring_start : substring_start + min_length]
