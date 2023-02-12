"""
Given a binary number represented as a linked list, return its decimal value.

Ex: Given the following linked list…

1 -> 0 -> 0 -> 1, return 9 (1001 in decimal is 9).
Ex: Given the following linked list…

0 -> 0 -> 1, return 1.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head:
            num = num * 2 + head.val
            head = head.next
        return num


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.getDecimalValue(ListNode(1, ListNode(0, ListNode(0, ListNode(1))))))
    print(solution.getDecimalValue(ListNode(0, ListNode(0, ListNode(1)))))
