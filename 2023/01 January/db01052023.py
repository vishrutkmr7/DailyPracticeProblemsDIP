"""
Given a sorted singly linked list, remove all duplicate values and return the modified list.

Ex: Given the following sorted singly linked list…

1->2->2->3, return a list that looks as follows: 1->2->3.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removeDuplicates(self, head):
        if not head:
            return head
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    print(solution.removeDuplicates(head).val)
