"""
This question is asked by Google.
Given a linked list and a value, remove all nodes containing the provided value,
and return the resulting list.

Ex: Given the following linked lists and values...

1->2->3->null, value = 3, return 1->2->null
8->1->1->4->12->null, value = 1, return 8->4->12->null
7->12->2->9->null, value = 7, return 12->2->9->null
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


def remove_nodes(lst, value):
    """
    This is an optimal solution.
    """
    if lst is None:
        return lst
    if lst.val == value:
        return remove_nodes(lst.next, value)
    lst.next = remove_nodes(lst.next, value)
    return lst


# Test Cases
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = None
remove_nodes(list1, 3).print_list()

list1 = ListNode(8)
list1.next = ListNode(1)
list1.next.next = ListNode(1)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(12)
list1.next.next.next.next.next = None
remove_nodes(list1, 1).print_list()

list1 = ListNode(7)
list1.next = ListNode(12)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(9)
list1.next.next.next.next = None
remove_nodes(list1, 7).print_list()
