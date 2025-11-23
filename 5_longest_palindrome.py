# Given a string s, return the longest palindromic substring in s.
# A palindrome is a string that reads the same forward and backward.
# The substring must be contiguous, and if multiple answers exist,
# return any one of them.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start, max_len = 0, 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    start = left
                    max_len = current_len
                left -= 1
                right += 1

        for i in range(len(s)):
            # Odd length palindrome (center on character)
            expand(i, i)
            # Even length palindrome (center between characters)
            expand(i, i + 1)

        return s[start:start + max_len]

