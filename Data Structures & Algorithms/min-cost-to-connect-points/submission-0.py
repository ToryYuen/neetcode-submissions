class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = collections.defaultdict(list)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])


        # Prim's
        res = 0
        minHeap = [[0, 0]]
        visit = set()
        while len(visit) < N:
            dist, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += dist
            visit.add(node)

            for d, n in adj[node]:
                if n not in visit:
                    heapq.heappush(minHeap, [d, n])
        return res
        