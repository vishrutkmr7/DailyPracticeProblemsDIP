# LinkedIn: Given a binary tree, find the most frequent subtree sum.


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def most_freq_subtree_sum(root):
    # fill this in.
    if root is None:
        return

    dist = {}

    def traverse(node):
        if not node.left and not node.right:
            if node.val not in dist:
                dist[node.val] = 0
            dist[node.val] += 1
            return node.val
        else:
            left = traverse(node.left) if node.left else 0
            right = traverse(node.right) if node.right else 0
            sum = node.val + left + right
            if sum not in dist:
                dist[sum] = 0
            dist[sum] += 1
            return sum

    s = traverse(root)
    maxCount = -1
    res = []
    for sum in dist:
        if dist[sum] > maxCount:
            res = [sum]
            maxCount = dist[sum]
        elif dist[sum] == maxCount:
            res.append(sum)

    return res[0]


root = Node(3, Node(1), Node(-3))
print(most_freq_subtree_sum(root))
# 1

