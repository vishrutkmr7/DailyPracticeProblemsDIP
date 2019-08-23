# This problem was recently asked by Uber:

# Given a linked list of integers, remove all consecutive nodes that sum up to 0.

class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def removeConsecutiveSumTo0(node):
    # Fill this in.
    start = node
    while start:
        total = 0
        cur = start.next

        while cur:
            total += cur.value
            if total == 0:
                start.next = cur.next
                break
                cur = cur.next
            else:
                start = start.next
    
    return start


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
    print (node.value, end=' ')
    node = node.next
# 10


# Unable to find optimum solution: Seeking assistance at
# https://stackoverflow.com/questions/57620642/how-to-delete-consecutive-elements-in-a-linked-list-which-add-up-to-0
