class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        visit.add((0, 0))

        DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minHeap = [(grid[0][0], 0, 0)] # (maxTime, r, c)
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == ROW - 1 and c == COL - 1:
                return t

            for x, y in DIRS:
                dr, dy = r + x, c + y
                if (dr >= ROW or dr < 0 or 
                dy >= COL or dy < 0 or 
                (dr, dy) in visit):
                    continue

                heapq.heappush(minHeap, (max(t, grid[dr][dy]), dr, dy))
                visit.add((dr, dy))
