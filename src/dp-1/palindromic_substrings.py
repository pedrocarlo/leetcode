# 647. Palindromic Substrings


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0

        # length 1 palindrome
        for i in range(n):
            dp[i][i] = True
            ans += 1

        # len 2 palindrome
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1

        # stride in chunks of 3 or more
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    ans += 1
                    dp[i][j] = True

        return ans


sol = Solution()
res = sol.countSubstrings("abc")
print(res)
