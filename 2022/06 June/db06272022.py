"""
Given an array of numbers sorted in ascending order,
return a height-balanced binary search tree using every number from the array.
Note: height-balanced meaning that the level of any node’s two subtrees should not differ by more than one.

Ex: Given the following nums...

nums = [1, 2, 3] return a reference to the following tree...
       2
      /  \
     1    3
Ex: Given the following nums...

nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
        3
       / \
      2   5
     /   / \
    1   4   6
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


def create_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = BinarySearchTree(nums[mid])
    root.left = create_bst(nums[:mid])
    root.right = create_bst(nums[mid + 1 :])
    return root


# Test cases
print(create_bst([1, 2, 3]))
print(create_bst([1, 2, 3, 4, 5, 6]))
