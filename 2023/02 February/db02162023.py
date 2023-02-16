"""
Given a reference to the head of a linked list and two values, m, and n, traverse the entire list keeping the first
m elements followed by removing the next n elements. Return the resulting list.

Ex: Given the following head, m, and n…

1 -> 2 -> 3 -> null, m = 1, n = 1, return 1 -> 3 -> null.
Ex: Given the following head, m, and n…

1 -> 3 -> 2 -> 4 -> null, m = 2, n = 2, return 1 -> 3 -> null.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def removeNodes(self, head: Node, m: int, n: int) -> Node:
        if not head:
            return head

        current = head
        while current:
            for _ in range(m - 1):
                if current:
                    current = current.next

            if not current:
                break

            temp = current.next
            for _ in range(n):
                if temp:
                    temp = temp.next

            current.next = temp
            current = temp

        return head


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    print(solution.removeNodes(head, 1, 1))

    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(2)
    head.next.next.next = Node(4)
    print(solution.removeNodes(head, 2, 2))
