"""
Given a binary tree, containing unique values, determine if it is a valid binary search tree.
Note: the invariants of a binary search tree (in our case) are all values to the left of a
given node are less than the current node’s value, all values to the right of a given node
are greater than the current node’s value, and both the left and right subtrees of a given
node must also be binary search trees. 

Ex: Given the following binary tree…

   1
 /   \
2     3
return false.
Ex: Given the following tree…

   2
 /   \
1     3
return true.
"""


class BinarySearchTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, arr):
        if not arr:
            return
        for val in arr:
            self.insert_helper(val)

    def insert_helper(self, val):
        if val < self.val:
            if self.left:
                self.left.insert_helper(val)
            else:
                self.left = BinarySearchTree(val)
        elif val > self.val:
            if self.right:
                self.right.insert_helper(val)
            else:
                self.right = BinarySearchTree(val)
        else:
            return


def is_valid_bst(tree):
    return is_valid_bst_helper(tree, float('-inf'), float('inf')) if tree else True


def is_valid_bst_helper(tree, min_val, max_val):
    if not tree:
        return True
    if tree.val < min_val or tree.val > max_val:
        return False
    return is_valid_bst_helper(tree.left, min_val, tree.val) and is_valid_bst_helper(tree.right, tree.val, max_val)


# Test Cases
tree = BinarySearchTree(1)
tree.insert([2, 3])
print(is_valid_bst(tree))

tree = BinarySearchTree(2)
tree.insert([1, 3])
print(is_valid_bst(tree))
