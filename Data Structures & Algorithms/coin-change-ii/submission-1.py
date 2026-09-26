class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 # one way for amount 1 

        for coin in coins:
            # amount starting from coin value 
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin] 
        
        return dp[amount]