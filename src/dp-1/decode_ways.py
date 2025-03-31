# 91. Decode Ways


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(1, n):
            if s[i + 1] != "0":
                dp[i + 1] += dp[i]
            if "10" <= s[i - 1 : i + 1] <= "26":
                dp[i + 1] += dp[i - 1]
        return dp[n]


sol = Solution()
# res = sol.numDecodings("12")
# print(res)

# res = sol.numDecodings("10")
# print(res)

# res = sol.numDecodings("26")
# print(res)

res = sol.numDecodings("226")
print(res)
