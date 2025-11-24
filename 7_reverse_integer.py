# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x results in a value outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], return 0 instead.
#
# The key constraint: we must NOT rely on 64-bit integer storage,
# so we manually check overflow BEFORE it happens.
#
# Approach:
# - Extract digits one-by-one using modulo and division.
# - Build the reversed number by multiplying the current result by 10 and adding the new digit.
# - Before each multiplication/addition, check if the operation would overflow.
# - If overflow would occur, return 0.

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   #  2147483647

        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow BEFORE multiplying by 10
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            rev = rev * 10 + digit

        return rev * sign

