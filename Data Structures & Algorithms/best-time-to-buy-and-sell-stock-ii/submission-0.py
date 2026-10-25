class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, bought):
            if i == len(prices):
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]

            res = dfs(i + 1, bought) # skip
            if bought:
                res = max(res, prices[i] + dfs(i + 1, False)) # sold
            else:
                res = max(res, -prices[i] + dfs(i + 1, True)) # bought
            dp[(i, bought)] = res
            return res
        return dfs(0, False)