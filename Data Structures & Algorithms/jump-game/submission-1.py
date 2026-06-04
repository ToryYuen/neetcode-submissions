class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= n:
                dp[i] = True
            else:
                dp[i] = False
                for j in range(i + 1, i + nums[i] + 1):
                    if dp[j] == True:
                        dp[i] = True
                        break

        return dp[0]
        