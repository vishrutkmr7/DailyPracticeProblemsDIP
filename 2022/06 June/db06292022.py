"""Given a binary search tree, return the minimum difference between any two nodes in the tree.

Ex: Given the following tree...
        2
       / \
      3   1
return 1.
Ex: Given the following tree...
        29
       /  \
     17   50
    /     / \
   1    42  59
return 8.
Ex: Given the following tree...
        2
         \
         100
return 98."""


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

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()


def inorderTraversal(root):
    res = []
    if root:
        res = inorderTraversal(root.left)
        res.append(root.value)
        res = res + inorderTraversal(root.right)
    return res


def min_difference_in_array(arr):
    min_diff = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < min_diff:
            min_diff = arr[i] - arr[i - 1]
    return min_diff


def find_min_diff(root):
    if root.left is None and root.right is None:
        return 0
    tree = inorderTraversal(root)
    return min_difference_in_array(tree)


# Test cases
tree = BinarySearchTree(2)
tree.insert(1)
tree.insert(3)
print(inorderTraversal(tree))
print(find_min_diff(tree))

tree = BinarySearchTree(29)
tree.insert(17)
tree.insert(50)
tree.insert(1)
tree.insert(42)
tree.insert(59)
print(inorderTraversal(tree))
print(find_min_diff(tree))

tree = BinarySearchTree(2)
tree.insert(100)
print(inorderTraversal(tree))
print(find_min_diff(tree))
