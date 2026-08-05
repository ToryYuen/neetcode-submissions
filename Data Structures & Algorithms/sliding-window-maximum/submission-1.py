class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for r in range(k):
            n = nums[r]
            heapq.heappush_max(heap, (n, r))
        
        l = 1
        res = [heap[0][0]]
        for r in range(k, len(nums)):
            while heap and heap[0][1] < l:
                heapq.heappop_max(heap)
            heapq.heappush_max(heap, (nums[r], r))
            res.append(heap[0][0])
            l += 1
        return res