class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for t in tasks:
            counts[t] = counts.get(t, 0) + 1
        
        maxHeap = [val for val in counts.values()]
        heapq.heapify_max(maxHeap)

        waiting = deque()
        time = 0

        while maxHeap or waiting:
            time += 1

            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt:
                    waiting.append([cnt, time + n])

            if waiting and waiting[0][1] == time:
                cnt = waiting.popleft()[0]
                heapq.heappush_max(maxHeap, cnt)
        return time