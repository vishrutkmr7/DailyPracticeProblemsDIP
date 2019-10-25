# This problem was recently asked by Microsoft:

# You are given a doubly linked list. Determine if it is a palindrome. Same for a singly linked list


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def traverse_list(node):
    l = []
    if node.val is None:
        print("List has no element")
        return
    else:
        n = node
        while n is not None:
            l.append(n.val)
            n = n.next

    return l


def is_palindrome(node):
    # Fill this in.
    l = traverse_list(node)
    if l == l[::-1]:
        return True
    return False


node = Node("a")
node.next = Node("b")
node.next.prev = node
node.next.next = Node("b")
node.next.next.prev = node.next
node.next.next.next = Node("a")
node.next.next.next.prev = node.next.next

print(is_palindrome(node))
# True
