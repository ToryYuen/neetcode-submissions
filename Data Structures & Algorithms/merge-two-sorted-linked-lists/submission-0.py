# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = node_pointer = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                node_pointer.next = list2
                list2 = list2.next
                node_pointer = node_pointer.next
            else:
                node_pointer.next = list1
                list1 = list1.next
                node_pointer = node_pointer.next
    
        node_pointer.next = list1 or list2

        return node.next