# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def add_two_ListNode(l1, l2, prevCarry):
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    
    sum = val1 + val2 + prevCarry
    carry = sum // 10
    remainder = sum % 10

    ln = ListNode(remainder)
    if carry or ((l1 and l1.next) or (l2 and l2.next)):
        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None
        ln.next = add_two_ListNode(next1, next2, carry)

    return ln


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return add_two_ListNode(l1, l2, 0)
