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

        index_to_remove = size - n
        if index_to_remove == 0:
            return head.next

        curr = head
        for i in range(size - 1):
            if (i + 1) == index_to_remove:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
        