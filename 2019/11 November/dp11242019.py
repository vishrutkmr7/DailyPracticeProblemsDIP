# This problem was recently asked by Apple:

# Given a binary tree, return the list of node values in zigzag order traversal


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_order(tree):
    # Fill this in.
    resArr = []
    if tree is None:
        return
    currentLevel = []
    nextLevel = []
    ltr = True

    currentLevel.append(tree)
    while len(currentLevel) > 0:
        temp = currentLevel.pop(-1)
        resArr.append(temp.value)

        if ltr:
            # ltr
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            # rtl
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        if len(currentLevel) == 0:
            ltr = not ltr
            currentLevel, nextLevel = nextLevel, currentLevel

    return resArr


n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]
