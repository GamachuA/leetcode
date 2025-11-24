# The string "PAYPALISHIRING" is written in a zigzag pattern across numRows.
# This solution uses the mathematical jump pattern for each row,
# but optimized to avoid slow string concatenation inside loops.
#
# Key Optimization:
#   Instead of doing 'res += char', we append characters to a list
#   and do ''.join(list) at the end. This avoids O(n²) behavior in Python.
#
# Time: O(n)
# Space: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = []  # list for efficient appending
        increment = 2 * (numRows - 1)

        # Process each row
        for r in range(numRows):
            for i in range(r, len(s), increment):
                result.append(s[i])  # vertical character

                # Add diagonal character for middle rows
                diag_index = i + increment - 2 * r
                if r > 0 and r < numRows - 1 and diag_index < len(s):
                    result.append(s[diag_index])

        return "".join(result)

