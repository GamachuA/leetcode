# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Implements Regular Expression Matching using Recursion with Memoization (Top-Down DP).
        The function starts the matching process from the end of both strings.
        """
        i, j = len(s) - 1, len(p) - 1
        # The cache stores results for the state (i, j)
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, cache, s, p, i, j):
        """
        Recursive helper function.
        i: current index in s (inclusive, 0-based)
        j: current index in p (inclusive, 0-based)
        """
        key = (i, j)
        if key in cache:
            # Check the cache before performing any complex logic
            return cache[key]
        
        # --- Base Cases ---

        # 1. SUCCESS: Both string and pattern are exhausted (match found)
        if i == -1 and j == -1:
            cache[key] = True
            return True

        # 2. FAILURE: Pattern exhausted but string is not
        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]

        # 3. Handle cases where the string is exhausted (i == -1)
        # We need to check if the remaining pattern (p[:j+1]) can match an empty string.
        if i == -1:
            # This only happens if the remaining pattern is entirely of the form 'char*'
            if p[j] == '*':
                # Try matching 0 occurrences of the preceding element
                # Equivalent to: dp[0][j] = dp[0][j-2]
                result = self.backtrack(cache, s, p, i, j - 2)
            else:
                # If the remaining pattern doesn't end in '*', it cannot match the empty string.
                result = False
            
            cache[key] = result
            return result
        
        # --- Recursive/Transition Logic ---

        # Case 1: Pattern character is '*'
        if p[j] == '*':
            # A. Match zero times (skip the previous char and '*')
            # Dependency: (i, j-2)
            if self.backtrack(cache, s, p, i, j - 2):
                cache[key] = True
                return True
            
            # B. Match one or more times (preceding char must match s[i])
            preceding_matches_s = (p[j - 1] == s[i] or p[j - 1] == '.')
            
            if preceding_matches_s:
                # '*' consumes s[i] and stays in place (j is unchanged) to potentially match more.
                # Dependency: (i-1, j)
                if self.backtrack(cache, s, p, i - 1, j):
                    cache[key] = True
                    return True
        
        # Case 2: Pattern character is '.' or matches s[i]
        elif p[j] == '.' or s[i] == p[j]:
            # Simple 1-to-1 match. Move back one index in both s and p.
            # Dependency: (i-1, j-1)
            if self.backtrack(cache, s, p, i - 1, j - 1):
                cache[key] = True
                return True

        # If none of the above conditions returned True, the current state (i, j) is False
        cache[key] = False
        return False


def main():
    """
    Main function to test the isMatch method.
    You can set breakpoints here and step into the 'isMatch' call.
    """
    solver = Solution()
    
    # --- Test Cases ---
    
    # 1. Basic Match
    s1, p1 = "aab", "c*a*b" # Expected: True
    # 2. Dot Match
    s2, p2 = "mississippi", "mis*is*ip*." # Expected: True
    # 3. Simple Mismatch
    s3, p3 = "ab", ".*c" # Expected: False
    # 4. Complex Star Match
    s4, p4 = "aaa", "a*a" # Expected: True
    
    print(f"s='{s1}', p='{p1}' -> Result: {solver.isMatch(s1, p1)}")
    print(f"s='{s2}', p='{p2}' -> Result: {solver.isMatch(s2, p2)}")
    print(f"s='{s3}', p='{p3}' -> Result: {solver.isMatch(s3, p3)}")
    print(f"s='{s4}', p='{p4}' -> Result: {solver.isMatch(s4, p4)}")


# This line ensures the main function runs when you execute the script
if __name__ == "__main__":
    main()
