# Apple: You are given a tree, and your job is to print it level-by-level with linebreaks.

from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        # Fill this in.
        # if self.val is None:
        #     return ""
        q = []
        q.append(self)
        ans = ""
        while q:
            count = len(q)
            while count > 0:
                temp = q.pop(0)
                print(temp.val, end=" ")
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                count -= 1
            print(" ")

        return ""


tree = Node("a")
tree.left = Node("b")
tree.right = Node("c")
tree.left.left = Node("d")
tree.left.right = Node("e")
tree.right.left = Node("f")
tree.right.right = Node("g")

print(tree)
# a
# bc
# defg
