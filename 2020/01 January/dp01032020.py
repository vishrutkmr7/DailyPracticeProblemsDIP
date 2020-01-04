# his problem was recently asked by Amazon:

# Given a sorted linked list of integers, remove all the duplicate elements in the linked list so that
# all elements in the linked list are unique.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_dup(lst):
    # Fill this in.
    temp1 = lst
    # Brute force dup delete: Better option: sort and delete
    while temp1 is not None and temp1.next is not None:
        temp2 = temp1
        while temp2.next is not None:
            if temp1.value == temp2.next.value:
                dup = temp2.next
                temp2.next = temp2.next.next
                del dup
            else:
                temp2 = temp2.next

        temp1 = temp1.next


lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))
