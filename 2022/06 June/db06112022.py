"""This question is asked by Facebook.
Given a linked list and a value n, remove the nth to last node and return the resulting list. 

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null
"""


from os import lstat


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


def remove_nth_to_last(lst, n):
    """
    This is an optimal solution.
    """
    fast = lst
    slow = lst

    for _ in range(n):
        fast = fast.next

    if not fast:
        return lst.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return lst


# Test Cases
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = None
remove_nth_to_last(list1, 1).print_list()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = None
remove_nth_to_last(list1, 2).print_list()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = None
remove_nth_to_last(list1, 3).print_list()
