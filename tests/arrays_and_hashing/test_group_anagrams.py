"""
Problem: Group Anagrams
"""

import unittest
from src.arrays_and_hashing.group_anagrams import GroupAnagrams


class TestGroupAnagrams(unittest.TestCase):
    """
    Test cases for group anagrams problem
    """

    def test_group_anagrams(self):
        sut = GroupAnagrams()
        self.assertCountEqual(
            map(
                set,
                sut.group_anagrams(
                    ["eat", "tea", "tan", "ate", "nat", "bat"],
                ),
            ),
            [
                set(["bat"]),
                set(["nat", "tan"]),
                set(["ate", "eat", "tea"]),
            ],
        )
        self.assertEqual(sut.group_anagrams([""]), [[""]])
        self.assertEqual(sut.group_anagrams(["a"]), [["a"]])
