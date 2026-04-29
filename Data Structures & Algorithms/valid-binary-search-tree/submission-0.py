# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def compare(root: Optional[TreeNode], low=-float('inf'), high=float('inf')):
            if not root:
                return True
             
            if not (low < root.val < high):
                return False

            return compare(root.left, low, root.val) and compare(root.right, root.val, high)

        return compare(root)
        