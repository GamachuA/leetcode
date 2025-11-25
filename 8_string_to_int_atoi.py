# Implement the myAtoi(string s) function, which converts a string into a
# 32-bit signed integer according to the following rules:
#
# 1. Whitespace:
#    - Ignore any leading spaces.
#
# 2. Signedness:
#    - Optional '+' or '-' determines sign.
#    - Default sign is positive.
#
# 3. Conversion:
#    - Read characters while they are digits.
#    - Stop at the first non-digit.
#    - Ignore leading zeros naturally (they have no effect in numeric building).
#    - If no digits appear, return 0.
#
# 4. Rounding (Overflow Handling):
#    - Clamp the number to 32-bit signed integer range:
#         - If result < -2^31: return -2^31
#         - If result >  2^31 - 1: return 2^31 - 1
#
# The environment does NOT allow storing or relying on 64-bit integers,
# so we must check overflow conditions *before* they happen when building
# the number from digits.
#
# Time: O(n)
# Space: O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   #  2147483647

        i = 0
        n = len(s)

        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # If we consumed all characters
        if i == n:
            return 0

        # 2. Handle sign
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        # 3. Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # Check overflow before it happens
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return result * sign

