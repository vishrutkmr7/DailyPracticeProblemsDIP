"""
This question is asked by Amazon.
Given a non-empty linked list, return the middle node of the list.
If the linked list contains an even number of elements, return the node closer to the end.
Ex: Given the following linked lists...

1->2->3->null, return 2
1->2->3->4->null, return 3
1->null, return 1
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


def middle_node(lst):
    """
    This is an optimal solution.
    """
    slow = lst
    fast = lst
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val


# Test Cases
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = None
print(middle_node(list1))

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = None
print(middle_node(list1))

list1 = ListNode(1)
list1.next = None
print(middle_node(list1))
