class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = {i: [] for i in range(n)}
        for node, edge in edges:
            nodes[node].append(edge)
            nodes[edge].append(node)

        visited = set()
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for connected in nodes[i]:
                dfs(connected)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count