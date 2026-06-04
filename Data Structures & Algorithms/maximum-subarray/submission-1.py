class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        prev = curr = max_val = nums[0]

        for i in range(1, len(nums)):
            curr = max(prev + nums[i], nums[i])
            max_val = max(max_val, curr)
            prev = curr

        return max_val

        