"""
Problem: Group Anagrams
Leetcode: https://leetcode.com/problems/group-anagrams/
Solution: Hashing
Time Complexity: O(n * klogk)
Space Complexity: O(n)
"""


from collections import defaultdict


class GroupAnagrams:
    """
    Problem: Group Anagrams
    """

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        """
        :param strs: list of strings
        :return: list of anagram groups
        """
        grouped = defaultdict[tuple[int, ...], list[str]](list)
        for s in strs:
            key = self._get_key(s)
            grouped[tuple(key)].append(s)
        return list(grouped.values())

    def _get_key(self, s: str) -> list[int]:
        result = [0] * 26
        for ch in s:
            result[ord(ch) - ord("a")] += 1
        return result
