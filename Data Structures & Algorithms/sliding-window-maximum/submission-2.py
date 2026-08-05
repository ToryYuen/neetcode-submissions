class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() #monotonic descreasing 
        l = 0
        res = []

        for r in range(len(nums)):
            while q and q[-1][0] < nums[r]:
                q.pop()
            q.append((nums[r], r))

            if q[0][1] < l:
                q.popleft()

            if (r + 1) >= k:
                res.append(q[0][0])
                l += 1
        return res       