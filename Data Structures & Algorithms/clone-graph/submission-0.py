"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node in copies:
                return copies[node]

            copy = Node(node.val)
            copies[node] = copy
            copy.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            return copy
        
        return dfs(node) if node is not None else None
        