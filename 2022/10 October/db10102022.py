"""
Given the reference to the root of a binary search tree and a target value,
return whether or not two individual values within the tree can sum to the target.

Ex: Given the following tree and target…

   1
  / \
 2   3, target = 4, return true.
Ex: Given the following tree and target…

   1
  / \
 2   3, target = 7, return false.
 """


from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_set = set()

        def target_sum(node, target):
            if not node:
                return False
            if node.val in hash_set:
                return True
            else:
                hash_set.add(target - node.val)
            return target_sum(node.left, k) or target_sum(node.right, k)

        return target_sum(root, k)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.findTarget(root, 4))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.findTarget(root, 7))
