"""
Given a binary tree, returns of all its levels in a bottom-up fashion
(i.e. last level towards the root). Ex: Given the following tree…

        2
       / \
      1   2
return [[1, 2], [2]]
Ex: Given the following tree…

       7
      / \
    6    2
   / \ 
  3   3 
return [[3, 3], [6, 2], [7]]
"""
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


def bottoms_up(root):
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
    return result[::-1]

# Test Cases
tree = BinarySearchTree(2)
tree.insert(1)
tree.insert(2)
print(bottoms_up(tree))

tree = BinarySearchTree(7)
tree.insert(6)
tree.insert(2)
tree.insert(3)
tree.insert(3)
print(bottoms_up(tree))