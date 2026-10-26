class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # store only the most 2 frequent num
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) < 3:
                continue

            new_count = defaultdict(int)
            for i, c in count.items():
                if c > 1:
                    new_count[i] = c - 1
            count = new_count
        
        res = []
        for n in count:
            if nums.count(n) > (len(nums) // 3):
                res.append(n)
        return res
