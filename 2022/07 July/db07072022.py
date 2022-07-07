"""
Given a binary tree, return its column order traversal from top to bottom and left to right.
Note: if two nodes are in the same row and column, order them from left to right.

Ex: Given the following tree…

    8
   / \
  2   29
     /  \
    3    9
return [[2], [8, 3], [29], [9]]
Ex: Given the following tree…

     100
    /   \
  53     78
 / \    /  \
32  3  9    20
return [[32], [53], [100, 3, 9], [78], [20]]
"""
import heapq as hq


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


def column_order(root):
    heap = []
    hq.heapify(heap)

    def dfs(root, depth, position):
        if not root:
            return

        hq.heappush(heap, (position, depth, root.val))
        dfs(root.left, depth + 1, position - 1)
        dfs(root.right, depth + 1, position + 1)
    
    dfs(root, 0, 0)
    result = []
    posHold = -float("inf")
    arrayHold = []

    while heap:
        pos, depth, val = hq.heappop(heap)
        # print((pos, depth, val))
        if pos != posHold:
            if len(arrayHold) > 0:
                result.append(arrayHold)
                arrayHold = []
            posHold = pos
        arrayHold.append(val)
    result.append(arrayHold)
    return result

# Test Cases
tree = BinaryTree(8)
tree.insert(2)
tree.insert(3)
tree.insert(29)
tree.insert(9)
print(column_order(tree))

tree = BinaryTree(100)
tree.insert(53)
tree.insert(78)
tree.insert(32)
tree.insert(3)
tree.insert(9)
tree.insert(20)
print(column_order(tree))
