class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # monotonic descreasing

        for r in range(k):
            while q and q[-1][0] < nums[r]:
                q.pop()
            q.append((nums[r], r))
        
        l = 1
        res = [q[0][0]]
        for r in range(k, len(nums)):
            while q and q[-1][0] < nums[r]:
                q.pop()
            q.append((nums[r], r))

            if q[0][1] < l:
                q.popleft()

            res.append(q[0][0])
            l += 1
        return res   