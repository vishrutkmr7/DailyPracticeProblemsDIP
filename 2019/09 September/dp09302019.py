# This problem was recently asked by Apple:

# You are given a binary tree representation of an arithmetic expression.
# In this tree, each leaf is an integer value,, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.
# Write a function that takes this tree and evaluates the expression.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    # Fill this in.
    if root is None:
        return 0
    if root.left is None and root.right is None: 
        return int(root.val)
    l = evaluate(root.left)
    r = evaluate(root.right)

    if root.val == '+':
        return l + r
    elif root.val == '-':
        return l - r
    elif root.val == '*':
        return l * r
    elif root.val == '/':
        return l / r

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print (evaluate(tree))
# 45
