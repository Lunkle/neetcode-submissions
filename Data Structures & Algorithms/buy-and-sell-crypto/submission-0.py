class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        profit = 0
        for i in reversed(prices):
            profit = max(profit, highest - i)
            highest = max(i, highest)
        return profit


        