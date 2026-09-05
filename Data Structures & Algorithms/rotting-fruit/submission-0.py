class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        fresh = 0

        def bfs(r, c):
            if (r < 0 or r >= ROWS or 
            c < 0 or c >= COLS or 
            (r, c) in visited or 
            grid[r][c] != 1):
                return

            grid[r][c] = 2
            nonlocal fresh
            fresh -= 1

            q.append((r, c))
            visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            minutes += 1

        return minutes if fresh == 0 else -1