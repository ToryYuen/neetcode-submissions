class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        dp = set()
        dp.add(0)
        target =  total // 2

        for n in nums:
            newDp = set()
            for prev in dp:
                newNum = prev + n
                if newNum == target:
                    return True
                elif newNum < target:
                    newDp.add(newNum)
                newDp.add(prev)
            dp = newDp
        return False