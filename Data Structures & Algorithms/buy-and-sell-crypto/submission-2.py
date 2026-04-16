class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftMin = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - leftMin)
            leftMin = min(leftMin, prices[i])
        return profit
        