from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy_price = prices[0]
        for p in prices[1:]:
            if min_buy_price > p:
                min_buy_price = p

            profit = max(profit, p - min_buy_price)
        return profit
