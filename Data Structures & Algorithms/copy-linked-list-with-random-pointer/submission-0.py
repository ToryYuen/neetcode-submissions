"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        source_to_copy = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            source_to_copy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = source_to_copy[curr]
            copy.next = source_to_copy[curr.next]
            copy.random = source_to_copy[curr.random]
            curr = curr.next

        return source_to_copy[head]