class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        res = 0
        while stones:
            if len(stones) == 1:
                res = heapq.heappop_max(stones)
                break
            
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)

            if y > x:
                heapq.heappush_max(stones, y - x)

        return res
        