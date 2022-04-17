#  This problem was recently asked by AirBNB:

# Given a linked list and a number k, rotate the linked list by k places.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current = self
        ret = ""
        while current:
            ret += str(current.value)
            current = current.next
        return ret


def rotate_list(list, k):
    # Fill this in.
    if k == 0:
        return

    current = list
    count = 1
    while count < k and current is not None:
        current = current.next
        count += 1

    if current is None:
        return

    kthNode = current
    while current.next is not None:
        current = current.next

    current.next = list
    list = kthNode.next
    kthNode.next = None

    return list


# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 2))
# 3412
