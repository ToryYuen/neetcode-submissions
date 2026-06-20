class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n
        xor_nums = 0

        for i in range(n):
            xor ^= i
            xor_nums ^= nums[i]
        
        return xor ^ xor_nums
        