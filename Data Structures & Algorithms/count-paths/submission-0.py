class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                if r == 0:
                   dp[r][c] = dp[r][c - 1]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c]
                else:
                    dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
        
        return dp[m-1][n-1]
                