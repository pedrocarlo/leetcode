# 5. Longest Palindromic Substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = (0, 0)

        for i in range(n):
            # Base case 1 sized is palindrome
            dp[i][i] = True

        # Base case where length = 2 is palindrome
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        # dp with length 3 palindrome and beyond
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]


sol = Solution()
res = sol.longestPalindrome("babad")
print(res)
