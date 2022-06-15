"""
This question is asked by Apple.
Given a potentially cyclical linked list where each value is unique,
return the node at which the cycle starts. If the list does not contain a cycle, return null.

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
"""


class ListNode:
    def __init__(self, node):
        self.val = node
        self.next = None

    def print_list(self):
        print(self.val)
        if self.next:
            self.next.print_list()
        else:
            print("null")


def has_cycle_value(lst):
    """
    This is an optimal solution.
    """
    slow = lst
    fast = lst
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow.next.val
    return None


# Test Cases
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
print(has_cycle_value(list1))

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = list1.next
print(has_cycle_value(list1))

list1 = ListNode(1)
list1.next = ListNode(9)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(7)
list1.next.next.next.next = list1.next.next
print(has_cycle_value(list1))
