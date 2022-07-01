'''
Given a binary tree, return its level order traversal where the nodes in each level
are ordered from left to right.

Ex: Given the following tree...

    4
   / \
  2   7
return [[4], [2, 7]]
Ex: Given the following tree...

    2
   / \
  10  15
        \
         20
return [[2], [10, 15], [20]]
Ex: Given the following tree...

    1
   / \
  9   32
 /      \
3        78
return [[1], [9, 32], [3, 78]]
'''


class BinarySearchTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.right is None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)


def levelOrder(root):
    queue = [(root, 0)]
    result = []
    total_level = 0
    if not root:
        return []
    while queue:
        node, level = queue.pop(0)
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1))
        if result and total_level < level or not result:
            result.append([node.val])
        else:
            result[-1].append(node.val)
        total_level = max(level, total_level)
    return result

# Test Cases
tree = BinarySearchTree(4)
tree.insert(2)
tree.insert(7)
print(levelOrder(tree))

tree = BinarySearchTree(2)
tree.insert(10)
tree.insert(15)
tree.insert(20)
print(levelOrder(tree))

tree = BinarySearchTree(1)
tree.insert(9)
tree.insert(32)
tree.insert(3)
tree.insert(78)
print(levelOrder(tree))
