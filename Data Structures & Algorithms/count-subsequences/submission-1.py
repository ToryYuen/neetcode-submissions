class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
        dp[len(s)][len(t)] = 1

        for r in range(len(s) + 1):
            dp[r][-1] = 1

        for r in range(len(s) - 1, -1, -1):
            for c in range(len(t) - 1, -1, -1):
                if s[r] == t[c]:
                    dp[r][c] = dp[r + 1][c] + dp[r + 1][c + 1]
                else:
                    dp[r][c] = dp[r + 1][c]
        return dp[0][0]
        