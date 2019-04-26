"""
By description, no need to validate 'n', but I did.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head

        l = head
        r = head

        i = 0
        while i < n and r is not None:
            r = r.next
            i += 1

        if r is None:
            if i == n:
                return head.next
            else:
                return head

        while r.next:
            l = l.next
            r = r.next

        l.next = l.next.next

        return head
