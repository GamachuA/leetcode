# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows.
#
# Example with numRows = 4:
# P     I     N
# A   L S   I G
# Y A   H R
# P     I
#
# Reading line by line gives: "PINALSIGYAHRPI"
#
# Goal:
#   Given a string s and an integer numRows,
#   simulate writing characters in a zigzag pattern,
#   then read the pattern row by row to form the final string.
#
# Approach:
#   - If numRows == 1 or s is too short, return s directly.
#   - Create a list of empty strings, each representing a row.
#   - Use a pointer "row" and a direction "step".
#   - Move row downwards until bottom row is reached,
#     then reverse direction and move upwards, repeating.
#   - Append each character of s to the correct row.
#   - Finally, join all rows into one combined string.
#
# Time: O(n)
# Space: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: no zigzag possible
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        step = 1  # +1 means moving down, -1 means moving up

        for char in s:
            rows[row] += char

            # If we hit top or bottom, reverse direction
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            # Move to next row
            row += step

        return "".join(rows)

