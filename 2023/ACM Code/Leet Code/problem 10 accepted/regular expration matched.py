class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize the DP table with False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Deals with patterns like "a*", "b*", etc.
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Populate the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        
        return dp[len(s)][len(p)]

# Example usage
solution = Solution()
s = "aa"
p = "a*"
print(solution.isMatch(s, p))  # Output: True
