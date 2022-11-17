"""
Given an n-ary tree, return a list containing the post order traversal of the tree.
Write your solution iteratively. 

Ex: Given the following n-ary tree...

        1
      / | \
     2  3  4, return [2, 3, 4, 1]
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def postorder(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(iter(node.children))
        return result[::-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.children = [TreeNode(2), TreeNode(3), TreeNode(4)]
    print(solution.postorder(root))
