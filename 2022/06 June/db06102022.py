"""
This question is asked by Apple.
Given two sorted linked lists,
merge them together in ascending order and return a reference to the merged list.

Ex: Given the following lists...

list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null
"""
# Definition for singly-linked list.
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

    def __str__(self):
        return str(self.val)


def merge_lists(lst1, lst2):
    """
    This is an optimal solution.
    """
    if lst1 is None:
        return lst2
    if lst2 is None:
        return lst1
    if lst1.val < lst2.val:
        lst1.next = merge_lists(lst1.next, lst2)
        return lst1
    else:
        lst2.next = merge_lists(lst1, lst2.next)
        return lst2


# Test Cases
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list2 = ListNode(4)
list2.next = ListNode(5)
list2.next.next = ListNode(6)
list2.next.next.next = None
merge_lists(list1, list2).print_list()

list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)
list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)
list2.next.next.next = None
merge_lists(list1, list2).print_list()

list1 = ListNode(4)
list1.next = ListNode(4)
list1.next.next = ListNode(7)
list2 = ListNode(1)
list2.next = ListNode(5)
list2.next.next = ListNode(6)
list2.next.next.next = None
merge_lists(list1, list2).print_list()
