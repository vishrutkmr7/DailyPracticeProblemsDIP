# This problem was recently asked by Apple:

# You are given two singly linked lists. The lists intersect at some node.
# Find, and return the node. Note: the lists are non-cyclical.

def intersection(a, b):
    # fill this in.

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def prettyPrint(self):
        c = self
        while c:
            print (c.val)
            c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4
