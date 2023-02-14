"""
Given an N-ary tree, return a list containing the preorder traversal of its elements.
Note: You may assume that each node in the tree has a children attribute to access all
of its N child nodes.

Ex: Given the following N-ary tree…

       1
     / | \
    2  3  4, return [1, 2, 3, 4].
Ex: Given the following N-ary tree…

       1
     /   \
    2     3 
        / | \
       4  7  9, return [1, 2, 3, 4, 7, 9].
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def preorder(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            stack.extend(iter(node.children[::-1]))
        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.children = [TreeNode(2), TreeNode(3), TreeNode(4)]
    print(solution.preorder(root))

    root = TreeNode(1)
    root.children = [TreeNode(2), TreeNode(3)]
    root.children[1].children = [TreeNode(4), TreeNode(7), TreeNode(9)]
    print(solution.preorder(root))
