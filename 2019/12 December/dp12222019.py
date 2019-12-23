# This problem was recently asked by Apple:

# Given 2 binary trees t and s, find if s has an equal subtree in t, where the structure and the values are the same.
# Return True if it exists, otherwise return False.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def areIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (
        root1.value == root2.value
        and areIdentical(root1.left, root2.left)
        and areIdentical(root1.right, root2.right)
    )


def find_subtree(s, t):
    # Fill this in.
    if s is None:
        return True

    if t is None:
        return False

    if areIdentical(t, s):
        return True

    return find_subtree(t.left, s) or find_subtree(t.right, s)


t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

print(find_subtree(s, t))
# True
