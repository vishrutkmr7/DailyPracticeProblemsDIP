"""
Given the reference to the root of a binary tree and the reference to the head of a linked list,
return whether or not the entire linked list appears as a subpath within the tree.

Ex: Given the following root and head…

      root = 1
            / \
           2   3
          /
         3
      head = 1 -> 2 -> 3, return true
Ex: Given the following root and head…

      root = 4
            / \
           2   7
          /
         3
      head = 2 -> 3 -> 4, return false.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        return (
            self.dfs(head, root)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
            if root
            else False
        )

    def dfs(self, head, root):
        if not head:
            return True
        if not root or root.val != head.val:
            return False
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.isSubPath(
            ListNode(1, ListNode(2, ListNode(3))),
            TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(3)),
        )
    )
    print(
        solution.isSubPath(
            ListNode(2, ListNode(3, ListNode(4))),
            TreeNode(4, TreeNode(2, TreeNode(3)), TreeNode(7)),
        )
    )
