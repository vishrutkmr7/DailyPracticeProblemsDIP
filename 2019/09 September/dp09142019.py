# This problem was recently asked by Microsoft:

# You are given the preorder and inorder traversals of a binary tree in the form of arrays.
# Write a function that reconstructs the tree represented by these traversals.

from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ""
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(inorder, preorder, inStrt, inEnd):
    # Fill this in.
    if inStrt > inEnd:
        return None

    tNode = Node(preorder[reconstruct.preIndex])
    reconstruct.preIndex += 1

    # If this node has no children then return
    if inStrt == inEnd:
        return tNode
    inIndex = search(inorder, inStrt, inEnd, tNode.val)
    tNode.left = reconstruct(inorder, preorder, inStrt, inIndex - 1)
    tNode.right = reconstruct(inorder, preorder, inIndex + 1, inEnd)

    return tNode


def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


preOrder = ["a", "b", "d", "e", "c", "f", "g"]
inOrder = ["d", "b", "e", "a", "f", "c", "g"]
reconstruct.preIndex = 0
tree = reconstruct(inOrder, preOrder, 0, len(inOrder) - 1)
print(tree)
# abcdefg
