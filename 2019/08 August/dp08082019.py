# This problem was recently asked by Apple:

# Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
  
def findCeilingFloor(root_node, k, floor=None, ceil=None):
    # Fill this in.
    if root_node is None:
        return None

    while root_node != None:
        if root_node.value == k:
            return (k, k)
        elif k < root_node.value:
            ceil = root_node
            root_node = root_node.left
        else:
            floor = root_node
            root_node = root_node.right

    return (floor.value, ceil.value)
  
root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
    
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print (findCeilingFloor(root, 5))
# (4, 6)