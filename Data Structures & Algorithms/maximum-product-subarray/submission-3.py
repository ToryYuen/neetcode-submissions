class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = dp_min = dp_max = nums[0]

        for i in range(1, len(nums)):
            dp_max_val = dp_max * nums[i]
            dp_min_val = dp_min * nums[i]

            dp_max = max(nums[i], dp_max_val, dp_min_val)
            dp_min = min(nums[i], dp_max_val, dp_min_val)

            max_product = max(max_product, dp_max)
        
        return max_product

