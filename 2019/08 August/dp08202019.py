# This problem was recently asked by Apple:

# You are given two singly linked lists. The lists intersect at some node.
# Find, and return the node. Note: the lists are non-cyclical.

def intersection(a, b):
    # fill this in.
    curA, curB = a, b
    lenA, lenB = 0, 0
    # Finding respective lengths
    while curA is not None:
        lenA += 1
        curA = curA.next

    while curB is not None:
        lenB += 1
        curB = curB.next

    curA, curB = a, b

    if lenA > lenB:
        for _ in range(lenA - lenB):
            curA = curA.next
    elif lenB > lenA:
        for _ in range(lenB - lenA):
            curB = curB.next

    while curB != curA:
            curB = curB.next
            curA = curA.next

    return curA

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print (c.val, end = ' ')
            # print(c.val),
            c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

# A = 1 -> 2 -> 3 -> 4
# B = 6 -> 3 -> 4 

c = intersection(a, b)
c.prettyPrint()
# 3 4
