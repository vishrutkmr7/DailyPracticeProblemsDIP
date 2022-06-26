"""
Given a binary search tree, rearrange the tree such that it forms a linked list where all its values are in ascending order.

Ex: Given the following tree...
        5
       / \
      1   6
return...

1
 \
  5
   \
    6
Ex: Given the following tree...

       5
      / \
    2    9
   / \ 
  1   3 
return...

1
 \
  2
   \
    3
     \
      5
       \
        9
Ex: Given the following tree...

5
 \
  6
return...

5
 \
  6
"""
# Defining a Binary Search Tree class
class BinarySearchTree:
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


def flatten_tree(tree):
    if tree is None:
        return
    flatten_tree(tree.left)
    flatten_tree(tree.right)
    if tree.left is not None:
        temp = tree.left
        while temp.right is not None:
            temp = temp.right
        temp.right = tree.right
        tree.right = tree.left
        tree.left = None
    return tree


# Test cases
bst1 = BinarySearchTree(5)
bst1.insert(1)
bst1.insert(6)
flatten_tree(bst1).print_tree()

bst2 = BinarySearchTree(5)
bst2.insert(2)
bst2.insert(9)
bst2.insert(1)
bst2.insert(3)
flatten_tree(bst2).print_tree()

bst3 = BinarySearchTree(5)
bst3.insert(6)
flatten_tree(bst3).print_tree()
