"""
This question is asked by Google.
Given the reference to the root of a binary search tree and a search value,
return the reference to the node that contains the value if it exists and null otherwise.
Note: all values in the binary search tree will be unique.

Ex: Given the tree...

        3
       / \
      1   4
and the search value 1 return a reference to the node containing 1.
Ex: Given the following tree...

        7
       / \
      5   9
         / \ 
        8   10
and the search value 9 return a reference to the node containing 9.
Ex: Given the following tree...

        8
       / \
      6   9
and the search value 7 return null.
"""


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


def search_bst(root, value):
    return root if root is not None and root.contains(value) else None


# Test cases
bst = BinarySearchTree(3)
bst.insert(1)
bst.insert(4)
print(search_bst(bst, 1))

bst = BinarySearchTree(7)
bst.insert(5)
bst.insert(9)
bst.insert(8)
bst.insert(10)
print(search_bst(bst, 9))

bst = BinarySearchTree(8)
bst.insert(6)
bst.insert(9)
print(search_bst(bst, 7))
