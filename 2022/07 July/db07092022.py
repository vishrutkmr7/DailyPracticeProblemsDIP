"""
Given a binary tree, return a list of strings containing all root to leaf paths. 

Ex: Given the following tree…

   1
 /   \
2     3
return ["1->2", "1->3"]
Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return ["8->2", "8->29->3", "8->29->9"]
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


def root_to_leaf(tree):
    if not tree:
        return []
    result = []
    path = []
    root_to_leaf_helper(tree, path, result)
    return result


def root_to_leaf_helper(tree, path, result):
    if not tree:
        return
    path.append(tree.val)
    if not tree.left and not tree.right:
        result.append('->'.join(map(str, path)))
    root_to_leaf_helper(tree.left, path, result)
    root_to_leaf_helper(tree.right, path, result)
    path.pop()


# Test Cases
tree = BinaryTree(1)
tree.insert(2)
tree.insert(3)
print(root_to_leaf(tree))

tree = BinaryTree(8)
tree.insert(2)
tree.insert(29)
tree.insert(3)
tree.insert(9)
print(root_to_leaf(tree))
