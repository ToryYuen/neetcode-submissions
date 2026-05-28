class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_array, min_array = [nums[0]] * len(nums), [nums[0]] * len(nums)
        max_val = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            max_array[i] = max(n, n * max_array[i - 1], n * min_array[i - 1])
            min_array[i] = min(n, n * max_array[i - 1], n * min_array[i - 1])
            max_val = max(max_val, max_array[i])
        
        return max_val

