# This problem was recently asked by LinkedIn:

# Given a sorted list of numbers, change it into a balanced binary search tree. You can assume there will be no duplicate numbers in the list.

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ""
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


def createBalancedBST(nums):
    # Fill this in.
    if not nums:
        return None

    mid = len(nums) / 2
    root = Node(nums[int(mid)])
    root.left = createBalancedBST(nums[: int(mid)])  # values < arr[mid]
    root.right = createBalancedBST(nums[int(mid) + 1 :])  # values > arr[mid]

    return root


print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
# / \ / \
# 1 3 5 7
