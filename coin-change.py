from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass

    def coinHelper(self, coins: List[int], amount: int) -> int:
        total = 0
        total_coins = 0
        coins.sort()
        coins.reverse()
        curr = amount
        for coin in coins:
            print("coin", coin)
            curr_amount = curr // coin
            print("curr_amount", curr_amount)

            total += curr_amount * coin
            curr -= curr_amount * coin

            total_coins += curr_amount

        return total_coins if total == amount else -1



sol = Solution()

print(sol.coinChange([186,419,83,408], 6249))
