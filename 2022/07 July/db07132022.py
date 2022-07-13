"""
Given two binary trees, return whether or not both trees have the same leaf sequence.
Two trees have the same leaf sequence if both trees’ leaves read the same from left to right. 

Ex: Given the following trees…

   1
 /   \
1     3
and


   7
 /   \
1     2
return false as both the trees' leaves don't read the same from left to right (i.e. [1, 3] and [1, 2]).
Ex: Given the following trees…

    8
   / \
  2   29
    /  \
   3    9
and

    8
   / \
  2  29
 /   /  \
2   3    9
     \
      3
return true as both the trees' leaves read the same from left to right (i.e. [2, 3, 9] and [2, 3, 9]).
"""


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(tree):
    return [tree.val] + dfs(tree.left) + dfs(tree.right) if tree else []


def is_same_leaf_sequence(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    return dfs(tree1) == dfs(tree2)


# Test Cases
tree1 = BinaryTree(1)
tree1.left = BinaryTree(1)
tree1.right = BinaryTree(3)

tree2 = BinaryTree(7)
tree2.left = BinaryTree(1)
tree2.right = BinaryTree(2)
print(is_same_leaf_sequence(tree1, tree2))

tree1 = BinaryTree(8)
tree1.left = BinaryTree(2)
tree1.right = BinaryTree(29)
tree1.right.left = BinaryTree(3)
tree1.right.right = BinaryTree(9)

tree2 = BinaryTree(8)
tree2.left = BinaryTree(2)
tree2.right = BinaryTree(29)
tree2.left.left = BinaryTree(2)
tree2.right.left = BinaryTree(3)
tree2.right.right = BinaryTree(9)
tree2.right.left.right = BinaryTree(3)
print(is_same_leaf_sequence(tree1, tree2))
