class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, curr = [], []

        def dfs(k, start, tmp_target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    curr.append(nums[i])
                    dfs(k - 1, i + 1, tmp_target - nums[i])
                    curr.pop()
                return

            # two sums
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < tmp_target:
                    l += 1
                elif nums[l] + nums[r] > tmp_target:
                    r -= 1
                else:
                    res.append(curr + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        dfs(4, 0, target)
        return res
