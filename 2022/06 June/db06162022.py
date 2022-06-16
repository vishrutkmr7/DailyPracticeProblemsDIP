"""
This question is asked by Facebook.
Given a linked list, containing unique values, reverse it, and return the result.

Ex: Given the following linked lists...

1->2->3->null, return a reference to the node that contains 3 which points to a list that looks like the following: 3->2->1->null
7->15->9->2->null, return a reference to the node that contains 2 which points to a list that looks like the following: 2->9->15->7->null
1->null, return a reference to the node that contains 1 which points to a list that looks like the following: 1->null
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


def reverse_list(lst):
    """
    This is an optimal solution.
    """
    prev = None
    curr = lst
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# Test Cases
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = None
reverse_list(list1).print_list()

list1 = ListNode(7)
list1.next = ListNode(15)
list1.next.next = ListNode(9)
list1.next.next.next = ListNode(2)
list1.next.next.next.next = None
reverse_list(list1).print_list()

list1 = ListNode(1)
list1.next = None
reverse_list(list1).print_list()
