"""
Problem: \
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0
    max_length = 0
    window_start = 0
    char_indexes = dict[str, int]()
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in char_indexes:
            window_start = max(window_start, char_indexes[right_char] + 1)
        char_indexes[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
