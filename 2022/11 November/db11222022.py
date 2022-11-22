"""
Given the reference to two linked lists, return the node at which they intersect.
Note: If the two lists never intersect, return null. 

Ex: Given the following linked lists...

A: A1->A2
          \
           C1->C2->C3
          /
B: B1->B2
return a reference to node C1.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
