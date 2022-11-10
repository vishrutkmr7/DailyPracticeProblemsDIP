"""
Given a reference to a binary tree, return the width of the tree.
The width of the tree is defined as the length of the longest path between any two nodes
in the tree. 
Note: The length of the longest path is measured by the number of edges between the two nodes. 

Ex: Given the following binary tree...

         1
       /   \
     3      9
    / \
   8   7, return 3 (there are three edges between 8->3->1->9 and 7->3->1->9).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        queue = [(root, 0)]
        while queue:
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            temp = []
            for node, i in queue:
                if node.left:
                    temp.append((node.left, 2 * i))
                if node.right:
                    temp.append((node.right, 2 * i + 1))
            queue = temp
        return ans


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.widthOfBinaryTree(
            TreeNode(1, TreeNode(3, TreeNode(8), TreeNode(7)), TreeNode(9))
        )
    )
