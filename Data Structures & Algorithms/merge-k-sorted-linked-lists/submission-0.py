# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = res_head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                res_head.next = list1
                list1 = list1.next
            else:
                res_head.next = list2
                list2 = list2.next
            res_head = res_head.next

        res_head.next = list1 or list2
        return res.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                temp.append(self.mergeTwoLists(l1, l2))
            lists = temp

        return lists[0]


        