"""
Given a binary tree and a target, return whether or not there exists
a root to leaf path such that all values along the path sum to the target. 

Ex: Given the following tree…

      1
     / \
    5   2
   /   / \
  1  12   29
and a target of 15, return true as the path 1->2->12 sums to 15.
Ex: Given the following tree…

     104
    /   \
  39     31
 / \    /  \
32  1  9    10
and a target of 175, return true as the path 104->39->32 sums to 175.
"""


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinaryTree(value)
        elif self.right:
            self.right.insert(value)
        else:
            self.right = BinaryTree(value)


def root_to_leaf_sum(tree, target):
    if not tree:
        return []
    result = []
    path = []
    root_to_leaf_helper(tree, path, result)
    return target in result


def root_to_leaf_helper(tree, path, result):
    if not tree:
        return
    path.append(tree.val)
    if not tree.left and not tree.right:
        result.append(sum(path))
    root_to_leaf_helper(tree.left, path, result)
    root_to_leaf_helper(tree.right, path, result)
    path.pop()


# Test Cases
tree = BinaryTree(1)
tree.insert(5)
tree.insert(2)
tree.insert(2)
tree.insert(1)
tree.insert(12)
tree.insert(29)
print(root_to_leaf_sum(tree, 15))

tree = BinaryTree(104)
tree.insert(39)
tree.insert(31)
tree.insert(32)
tree.insert(1)
tree.insert(9)
tree.insert(10)
print(root_to_leaf_sum(tree, 175))
