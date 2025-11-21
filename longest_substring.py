# Given a string s, find the length of the longest substring without repeating characters.
# Return the length of this longest substring.
# The substring must consist of consecutive characters and contain no duplicates.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # stores character -> latest index
        left = 0         # left pointer of sliding window
        max_len = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # move left pointer past duplicate

            char_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len

