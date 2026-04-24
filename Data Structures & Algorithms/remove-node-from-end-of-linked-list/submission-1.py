# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        index = 0
        index_to_remove = size - n
        prev, curr = None, head
        while index != index_to_remove:
            prev = curr
            curr = curr.next
            index += 1
        
        if prev is None:
            return head.next
        prev.next = curr.next
        return head

        