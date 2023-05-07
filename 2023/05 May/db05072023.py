"""
Given the reference to a linked list, head, swap each pair of adjacent nodes
and the return a reference to the modified list.

Ex: Given a reference to the following linked list…

1->2->3->4, return 2->1->4->3 (1 and 2 have been swapped and 3 and 4 have been swapped).
"""

from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, cur, ans = None, head, head.next
        while cur and cur.next:
            adj = cur.next
            if prev:
                prev.next = adj

            cur.next, adj.next = adj.next, cur
            prev, cur = cur, cur.next

        return ans or head


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    ans = sol.swapPairs(head)
    while ans:
        print(ans.val, end=" ")
        ans = ans.next
