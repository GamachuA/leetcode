# 10. Regular Expression Matching
# Problem:
# Given an input string s and a pattern p, implement regular expression matching
# with support for the following special characters:
#
#   '.' -> Matches any single character.
#   '*' -> Matches zero or more of the preceding element.
#
# The matching must cover the *entire* input string (not partial).
#
# Examples:
#   s = "aa", p = "a"       -> False
#   s = "aa", p = "a*"      -> True  (zero or more 'a')
#   s = "ab", p = ".*"      -> True  (any characters)
#
# Approach:
# Use dynamic programming.
#
# Let dp[i][j] represent whether s[:i] matches p[:j].
# We build a 2D DP table where:
#
# Case 1: If characters match (or pattern has '.'):
#     dp[i][j] = dp[i-1][j-1]
#
# Case 2: If pattern has '*':
#     '*' means "zero or more" of p[j-2]
#
#     Two possibilities:
#       a) Zero occurrences:
#            dp[i][j] = dp[i][j-2]
#
#       b) One or more occurrences (only if chars match):
#            dp[i][j] = dp[i-1][j]
#
# Final answer = dp[len(s)][len(p)]
#
# Time Complexity: O(len(s) * len(p))
# Space Complexity: O(len(s) * len(p))

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, .*b* etc. that can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                # Direct character match or '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                
                # '*' case
                elif p[j - 1] == '*':
                    # Case a: zero occurrences of preceding char
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case b: one/more occurrences (match required)
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[m][n]

