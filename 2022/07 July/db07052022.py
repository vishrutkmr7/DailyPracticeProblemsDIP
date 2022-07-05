'''
Given a binary tree, return its zig-zag level order traversal
(i.e. its level order traversal from left to right the first level, right to left the level the second, etc.).

Ex: Given the following tree…

    1
   / \
  2   3
return [[1], [3, 2]]
Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return [[8], [29, 2], [3, 9]]
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


def zigzag(root):
    levels = levelOrder(root)
    for i in range(len(levels)):
        if i % 2 != 0:
            levels[i] = levels[i][::-1]
    return levels


# Test cases
tree = BinarySearchTree(8)
tree.insert(2)
tree.insert(29)
tree.insert(3)
tree.insert(9)
print(zigzag(tree))

tree = BinarySearchTree(1)
tree.insert(2)
tree.insert(3)
print(zigzag(tree))
