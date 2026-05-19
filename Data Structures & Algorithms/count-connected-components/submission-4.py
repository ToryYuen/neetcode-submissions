class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            curr = node
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr

        def union(u, v):
            u_parent = find(u)
            v_parent = find(v)

            if u_parent == v_parent:
                return False

            if rank[u_parent] < rank[v_parent]:
                u_parent, v_parent = v_parent, u_parent

            parent[v_parent] = u_parent
            rank[u_parent] += rank[v_parent]
            return True

        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        return res
        