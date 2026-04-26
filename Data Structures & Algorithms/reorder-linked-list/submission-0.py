# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> None:
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        mid = n // 2
        mid_idx = 0
        mid_pt = head
        while mid_idx != mid:
            mid_pt = mid_pt.next
            mid_idx += 1

        mid_next = mid_pt.next
        mid_pt.next = None
        reversed_mid_pt = self.reverse(mid_next)     

        while reversed_mid_pt:
            tmp = head.next
            reversed_tmp = reversed_mid_pt.next
            head.next = reversed_mid_pt
            head.next.next = tmp
            head = head.next.next
            reversed_mid_pt = reversed_tmp


        