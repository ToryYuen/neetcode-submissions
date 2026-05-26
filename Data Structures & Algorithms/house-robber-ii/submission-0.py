class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])

        def find_max(n: List[int]) -> int:
            dp = [0] * len(n)
            dp[0], dp[1] = n[0], max(n[0], n[1])

            for i in range(2, len(n)):
                dp[i] = max(dp[i - 2] + n[i], dp[i - 1])

            return dp[-1]

        return max(find_max(nums[1:length]), find_max(nums[:length - 1]))
        