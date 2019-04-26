"""
Interpret this problem as the middle of divide and conquer for merge sort,
especially as conquering procedure.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy

        while l1 is not None or l2 is not None:
            if l1 is None:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next

            curr = curr.next

        return dummy.next


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return []

        result = lists
        interval = 1
        while interval < len(result):
            for i in range(0, len(result) - interval, interval * 2):
                result[i] = self.mergeTwoList(result[i], result[i + interval])
            interval *= 2

        return result[0]
