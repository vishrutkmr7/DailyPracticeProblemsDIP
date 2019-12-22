# This problem was recently asked by Microsoft:

# Given a binary tree, find the level in the tree where the sum of all nodes on that level is the greatest.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def tree_level_max_sum(root):
    # Fill this in.
    if root is None:
        return 0
    maxLevel = 1
    level = 0
    maxSum = root.val
    q = []
    q.append(root)
    while len(q) is not 0:
        levelSum = 0
        size = len(q)

        for i in range(0, size):
            n = q[i]

            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)

            levelSum += n.val

        q.pop(0)

        if levelSum > maxSum:
            maxSum = levelSum
            maxLevel = level

        level += 1

    return maxLevel


n3 = Node(4, Node(3), Node(2))
n2 = Node(5, Node(4), Node(-1))
n1 = Node(1, n2, n3)

"""
    1          Level 0 - Sum: 1
   / \
  4   5        Level 1 - Sum: 9 
 / \ / \
3  2 4 -1      Level 2 - Sum: 8

"""

print(tree_level_max_sum(n1))
# Should print 1 as level 1 has the highest level sum
