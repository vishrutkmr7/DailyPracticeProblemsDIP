"""
Given a binary search tree that contains unique values and two nodes within the tree, a, and b, return their lowest common ancestor.
Note: the lowest common ancestor of two nodes is the deepest node within the tree such that both nodes are descendants of it.

Ex: Given the following tree...
       7
      / \
    2    9
   / \ 
  1   5 
and a = 1, b = 9, return a reference to the node containing 7.
Ex: Given the following tree...

        8
       / \
      3   9
     / \ 
    2   6
and a = 2, b = 6, return a reference to the node containing 3.
Ex: Given the following tree...

        8
       / \
      6   9
and a = 6, b = 8, return a reference to the node containing 8.
"""


class BinarySearchTree:
    """Binary Search Tree class"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.right is None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            return False if self.left is None else self.left.contains(value)
        else:
            return False if self.right is None else self.right.contains(value)

    def get_max(self):
        return self.value if self.right is None else self.right.get_max()

    def get_min(self):
        return self.value if self.left is None else self.left.get_min()

    def get_max_depth(self):
        return 1 if self.right is None else 1 + self.right.get_max_depth()

    def get_min_depth(self):
        return 1 if self.left is None else 1 + self.left.get_min_depth()

    def get_size(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_size()
        elif self.right is None:
            return 1 + self.left.get_size()
        else:
            return 1 + self.left.get_size() + self.right.get_size()

    def get_height(self):
        if self.left is None:
            return 1 + self.right.get_height()
        elif self.right is None:
            return 1 + self.left.get_height()
        else:
            return 1 + max(self.left.get_height(), self.right.get_height())

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()


def least_common_ancestors(tree, a, b):
    """
    :param tree: BinarySearchTree
    :param a: int
    :param b: int
    :return: BinarySearchTree
    """
    if tree is None:
        return None
    if tree.value in [a, b]:
        return tree
    left = least_common_ancestors(tree.left, a, b)
    right = least_common_ancestors(tree.right, a, b)
    return tree if left and right else left or right

# Test cases
tree = BinarySearchTree(7)
tree.insert(2)
tree.insert(9)
tree.insert(1)
tree.insert(5)
print(least_common_ancestors(tree, 1, 9).value)

tree = BinarySearchTree(8)
tree.insert(3)
tree.insert(9)
tree.insert(2)
tree.insert(6)
print(least_common_ancestors(tree, 2, 6).value)

tree = BinarySearchTree(8)
tree.insert(6)
tree.insert(9)
print(least_common_ancestors(tree, 6, 8).value)