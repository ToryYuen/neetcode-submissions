class Solution:
    def find_pivot(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l


    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)

        l, r = 0, len(nums) - 1
        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1