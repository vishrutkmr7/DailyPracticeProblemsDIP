"""
Given a binary search tree, return its mode
(you may assume the answer is unique). If the tree is empty, return -1.
Note: the mode is the most frequently occurring value in the tree.

Ex: Given the following tree...

        2
       / \
      1   2
return 2.

Ex: Given the following tree...

         7
        / \
      4     9
     / \   / \
    1   4 8   9
               \
                9  
return 9.
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


def inorderTraversal(root):
    res = []
    if root:
        res = inorderTraversal(root.left)
        res.append(root.value)
        res = res + inorderTraversal(root.right)
    return res


def BST_Mode(root):
    if root is None:
        return -1
    arr = inorderTraversal(root)
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_val = max(d.values())
    for key, value in d.items():
        if value == max_val:
            return key

# Test cases
tree = BinarySearchTree(2)
tree.insert(1)
tree.insert(2)
print(BST_Mode(tree))

tree = BinarySearchTree(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(4)
tree.insert(8)
tree.insert(9)
tree.insert(9)
print(BST_Mode(tree))
