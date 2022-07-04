'''
Given a binary tree return all the values you’d be able to see
if you were standing on the left side of it with values ordered from top to bottom.

Ex: Given the following tree…

-->    4
      / \
-->  2   7
return [4, 2]
Ex: Given the following tree…

-->        7
         /  \
-->     4     9
       / \   / \
-->   1   4 8   9
                 \
-->               9
return [7, 4, 1, 9]
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

def visible_values(root):
    levels = levelOrder(root)
    return [level[0] for level in levels]

# Test Cases
tree = BinarySearchTree(4)
tree.insert(2)
tree.insert(7)
print(visible_values(tree))

tree = BinarySearchTree(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(4)
tree.insert(8)
tree.insert(9)
# tree.insert(None)
tree.insert(9)
print(visible_values(tree))