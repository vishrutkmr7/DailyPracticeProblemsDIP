# This problem was recently asked by Microsoft:

# A unival tree is a tree where all the nodes have the same value.
# Given a binary tree, return the number of unival subtrees in the tree.

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_unival_subtrees(root):
    # Fill this in.
    count = [0]
    countrec(root, count)
    return count[0]

def countrec(root, count):
    if root is None:
        return True
    
    left = countrec(root.left, count)
    right = countrec(root.right, count)

    if left == False or right == False:
        return False
    
    if root.left and root.val != root.left.val: 
        return False 
    if root.right and root.val != root.right.val: 
        return False

    count[0] += 1
    return True

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print (count_unival_subtrees(a))
# 5
