'''
Given a binary tree, return the largest value in each of its levels. Ex: Given the following tree…

    2
   / \
  10  15
        \
         20
return [2, 15, 20]
Ex: Given the following tree…

          1
         / \
        5   6
       / \   \  
      5   3   7 
return [1, 6, 7]
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

def max_at_level(root):
    levels = levelOrder(root)
    return [max(level) for level in levels]

# Test cases
tree = BinarySearchTree(2)
tree.insert(10)
tree.insert(15)
tree.insert(0)
tree.insert(0)
tree.insert(20)
print(max_at_level(tree))

tree = BinarySearchTree(1)
tree.insert(5)
tree.insert(6)
tree.insert(5)
tree.insert(3)
tree.insert(7)
print(max_at_level(tree))