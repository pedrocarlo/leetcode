# https://www.fastprep.io/problems/citadel-maximize-the-lottery-id

# incorrect Claude solution. Should be 5
class Solution:
    def maximizeLotteryID(self, lotteryID: str, winnerID: str, k: int) -> int:
        # Convert to lowercase for case-insensitive comparison
        m, n = len(lotteryID), len(winnerID)

        # Initialize a 3D DP array:
        # dp[i][j][r] = maximum LCS between lotteryID[0...i-1] and winnerID[0...j-1]
        # with at most r operations remaining
        dp = [[[0 for _ in range(k + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

        # Fill the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for r in range(k + 1):  # r = remaining operations
                    # Option 1: Skip current characters
                    dp[i][j][r] = max(dp[i - 1][j][r], dp[i][j - 1][r])

                    # Option 2: Characters match naturally - include in LCS
                    if lotteryID[i - 1] == winnerID[j - 1]:
                        dp[i][j][r] = max(dp[i][j][r], dp[i - 1][j - 1][r] + 1)

                    # Option 3: Use an operation to modify lotteryID[i-1]
                    if r > 0:
                        # Check if we can change lotteryID[i-1] to match winnerID[j-1] in one step
                        lottery_char = ord(lotteryID[i - 1].lower())
                        winner_char = ord(winnerID[j - 1].lower())

                        # Check if characters are within the a-z range
                        if (
                            "a" <= lotteryID[i - 1].lower() <= "z"
                            and "a" <= winnerID[j - 1].lower() <= "z"
                        ):
                            # Check if we can transform with one operation (next or previous)
                            diff = (winner_char - lottery_char) % 26
                            if (
                                diff == 1 or diff == 25
                            ):  # next (1) or previous (25 or -1 in modular arithmetic)
                                dp[i][j][r] = max(
                                    dp[i][j][r], dp[i - 1][j - 1][r - 1] + 1
                                )

        return dp[m][n][k]


lotteryID = "fpeIqanxyk"
winnerID = "hackerrank"
k = 6

sol = Solution()
result = sol.maximizeLotteryID(lotteryID.lower(), winnerID.lower(), k)
print(f"Maximum LCS length after at most {k} operations: {result}")
