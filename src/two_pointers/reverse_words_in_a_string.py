"""
Problem: Reverse Words in a String
Leetcode: https://leetcode.com/problems/reverse-words-in-a-string/
"""

from abc import ABC, abstractmethod


class Solution(ABC):
    @abstractmethod
    def reverse_words(self, s: str) -> str:
        pass


def _reverse(s: list[str], start: int, end: int):
    while start < end:
        temp = s[end]
        s[end] = s[start]
        s[start] = temp
        start += 1
        end -= 1


class TwoPointersSolution(Solution):
    def reverse_words(self, s: str) -> str:
        words = list(filter(lambda element: element, s.split(" ")))
        sentence = list(" ".join(words))
        n = len(sentence)
        _reverse(sentence, 0, n - 1)
        start = 0
        end = 0
        while start <= end < n:
            while end < n and sentence[end] != " ":
                end += 1
            _reverse(sentence, start, end - 1)
            start, end = end + 1, end + 2
        return "".join(sentence)
