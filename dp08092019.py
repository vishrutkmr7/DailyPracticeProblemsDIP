# This problem was recently asked by Twitter:

# You are given the root of a binary tree. Invert the binary tree in place. That is, all left children should become right children, and all right children should become left children.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def preorder(self):
        print (self.value),
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()
  
def invert(node):
  # Fill this in.
  if node:
    node.left, node.right = invert(node.right), invert(node.left)
    return node

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print ("\n")
invert(root)
root.preorder()
# a c f b e d

# P.S, Just leaving a link to Max Howell's tweet about this problem
# https://twitter.com/mxcl/status/608682016205344768?lang=en