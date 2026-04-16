class Solution:
    def bin_search(self, nums: List[int], target: int, l:int, r:int):
        if l > r:
            return -1
        
        idx = l + ((r-l) // 2)
        mid = nums[idx]
        
        if mid == target:
            return idx
        elif mid > target:
            return self.bin_search(nums, target, l, idx-1)
        else:
            return self.bin_search(nums, target, idx+1, r)

        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, target, 0, len(nums)-1)