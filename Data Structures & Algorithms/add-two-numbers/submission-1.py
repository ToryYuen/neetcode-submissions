# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = ListNode()
        np = n
        carry = 0
        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            
            new = ListNode(val)
            np.next = new

            np = np.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            np.next = ListNode(1)
        return n.next
