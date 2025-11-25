# 9. Palindrome Number
# Problem:
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# A palindrome number reads the same backward as forward.
# Negative numbers are not palindromes, and numbers ending in 0 (except 0 itself)
# cannot be palindromes. Solve it without converting the integer to a string.
#
# Approach:
# Reverse only half of the number and compare the two halves.
# This avoids potential overflow (in other languages) and keeps the solution O(1) space.
#
# Steps:
# 1. Negative numbers -> False.
# 2. If last digit is 0 but number is not 0 -> False.
# 3. Reverse digits from the right until reversed_half >= x.
# 4. Compare:
#    - For even length: x == reversed_half
#    - For odd length:  x == reversed_half // 10
#
# Time Complexity: O(log10 n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_half = 0
        
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10

