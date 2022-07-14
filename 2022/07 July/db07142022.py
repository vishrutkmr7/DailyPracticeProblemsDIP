'''
Given a binary tree, return the sum of all left leaves of the tree.
Ex: Given the following tree…

    5
   / \
  2   12
     /  \
    3    8
return 5 (i.e. 2 + 3)
Ex: Given the following tree…

       2
      / \
    4    2
   / \ 
  3   9 
return 3
'''


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_left_leaf_sum(tree):
    if not tree:
        return 0
    if tree.left and not tree.left.left and not tree.left.right:
        return tree.left.val + get_left_leaf_sum(tree.right)
    else:
        return get_left_leaf_sum(tree.left) + get_left_leaf_sum(tree.right)


# Test Cases
tree1 = BinaryTree(5)
tree1.left = BinaryTree(2)
tree1.right = BinaryTree(12)
tree1.right.left = BinaryTree(3)
tree1.right.right = BinaryTree(8)
print(get_left_leaf_sum(tree1))

tree2 = BinaryTree(2)
tree2.left = BinaryTree(4)
tree2.right = BinaryTree(2)
tree2.left.left = BinaryTree(3)
tree2.left.right = BinaryTree(9)
print(get_left_leaf_sum(tree2))
