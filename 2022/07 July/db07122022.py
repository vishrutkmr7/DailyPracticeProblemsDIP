"""
Given a binary tree, return whether or not it forms a reflection across its center
(i.e. a line drawn straight down starting from the root). 
Note: a reflection is when an image, flipped across a specified line, forms the same image.

Ex: Given the following tree…

   2
 /   \
1     1
return true as when the tree is reflected across its center all the nodes match.
Ex: Given the following tree…

    1
   / \
  5   5
   \    \
    7    7
return false as when the tree is reflected across its center the nodes containing sevens do not match.
"""


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_symmetric(tree):
    return is_symmetric_helper(tree, tree)


def is_symmetric_helper(tree1, tree2):
    if tree1 or tree2:
        return (
            False
            if not tree1 or not tree2
            else tree1.val == tree2.val
            and is_symmetric_helper(tree1.left, tree2.right)
            and is_symmetric_helper(tree1.right, tree2.left)
        )

    else:
        return True


# Test Cases
tree = BinaryTree(2)
tree.left = BinaryTree(1)
tree.right = BinaryTree(1)
print(is_symmetric(tree))

tree = BinaryTree(1)
tree.left = BinaryTree(5)
tree.right = BinaryTree(5)
tree.left.right = BinaryTree(7)
tree.right.right = BinaryTree(7)
print(is_symmetric(tree))
