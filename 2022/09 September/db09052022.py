"""
This question is asked by Google.
Given an N-ary tree, return its maximum depth.
Note: An N-ary tree is a tree in which any node may have at most N children.

Ex: Given the following tree…

            4
          / | \
         3  9  2
        /       \
       7         2
return 3.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if root is None:
            return 0
        if root.children is None:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = Node(4, [Node(3, [Node(7)]), Node(9), Node(2, [Node(2)])])
    print(solution.maxDepth(root))
