# This problem was recently asked by Amazon:

# Given a number n, generate all binary search trees that can be constructed with nodes 1 to n.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        result = str(self.value)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result


def generate_bst(s, n):
    # Fill this in.
    lst = []
    if s > n:
        lst.append(None)
        return lst
    for i in range(s, n + 1):
        leftSubtree = generate_bst(s, i - 1)
        rightSubtree = generate_bst(i + 1, n)
        for j in range(len(leftSubtree)):
            left = leftSubtree[j]
            for k in range(len(rightSubtree)):
                right = rightSubtree[k]
                node = Node(i)  # making value i as root
                node.left = left  # connect left subtree
                node.right = right  # connect right subtree
                lst.append(node)  # add this tree to list
    return lst


for tree in generate_bst(1, 3):
    print(tree)

# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1
