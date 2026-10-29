class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        store info in the original list:
            mark the index column as -ve if the value in range and exist
        '''

        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0

        # [3,4,-1,1] -> [-3,4,-inf,-1]
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0: # value exists
                    nums[val - 1] *= -1 #mark the index column as -ve
                elif nums[val - 1] == 0: 
                    # originally -ve, any value that not in range 1 <= val <= len(nums)
                    nums[val - 1] = -float('inf') 
                
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1
        