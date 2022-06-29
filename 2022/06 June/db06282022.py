"""
Given two binary trees, return whether or not the two trees are identical.
Note: identical meaning they exhibit the same structure and the same values at each node.
Ex: Given the following trees...

        2
       / \
      1   3
    2
   / \
  1   3

return true.
Ex: Given the following trees...

        1
         \
          9
           \
           18
    1
   /
  9
   \
    18

return false.
Ex: Given the following trees...

        2
       / \
      3   1
    2
   / \
  1   3

return false.
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


# Check if 2 BST's are identical
def check_identical(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is None or tree2 is None or tree1.value != tree2.value:
        return False
    else:
        return check_identical(tree1.left, tree2.left) and check_identical(
            tree1.right, tree2.right
        )

# Test cases
tree1 = BinarySearchTree(2)
tree1.insert(1)
tree1.insert(3)
tree2 = BinarySearchTree(2)
tree2.insert(1)
tree2.insert(3)
print(check_identical(tree1, tree2))

tree1 = BinarySearchTree(1)
tree1.insert(9)
tree1.insert(18)
tree2 = BinarySearchTree(1)
# tree2.insert(None)
tree2.insert(9)
tree2.insert(18)
print(check_identical(tree1, tree2))

tree1 = BinarySearchTree(2)
tree1.insert(3)
tree1.insert(1)
tree2 = BinarySearchTree(2)
tree2.insert(1)
tree2.insert(3)
print(check_identical(tree1, tree2))
