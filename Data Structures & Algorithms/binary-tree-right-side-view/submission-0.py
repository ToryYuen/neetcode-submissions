# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        def bfs():
            while q:
                rightMost = None
                length = len(q)

                for i in range(length):
                    node = q.popleft()
                    if node:
                        rightMost = node
                        q.append(node.left)
                        q.append(node.right)

                if rightMost:
                    res.append(rightMost.val)
        
        bfs()
        return res