"""
This question is asked by Facebook.
Given a singly linked list, re-order and group its nodes in such a way that the nodes
in odd positions come first and the nodes in even positions come last.

Ex: Given the reference to the following linked list...

4->7->5->6->3->2->1->NULL, return 4->5->3->1->7->6->2->NULL
Ex: Given the reference to the following linked list...

1->2->3->4->5->NULL, return 1->3->5->2->4->NULL
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def solve(self, head):
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.solve(Node(4, Node(7, Node(5, Node(6, Node(3, Node(2, Node(1)))))))))
    print(solution.solve(Node(1, Node(2, Node(3, Node(4, Node(5)))))))
