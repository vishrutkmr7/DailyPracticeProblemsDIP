'''
Given an n-ary tree, return its level order traversal. 
Note: an n-ary tree is a tree in which each node has no more than N children. 

Ex: Give the following n-ary tree…

    8
  / | \
 2  3  29
return [[8], [2, 3, 29]]
Ex: Given the following n-ary tree…

     2
   / | \
  1  6  9
 /   |   \
8    2    2
   / | \
 19 12 90
return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]
'''
class nAryTree:
    def __init__(self, val):
        self.val = val
        self.children = []

    def insert(self, value):
        self.children.append(nAryTree(value))

def nAry_Levelorder(root):
    hashMap = {}
    queue = [(root, 0)] if root else []
    while queue:
        node, lvl = queue.pop(0)
        hashMap[lvl] = hashMap.get(lvl,[]) + [node.val]
        queue.extend((child, lvl+1) for child in node.children)
    return list(hashMap.values())

# Test Cases
tree = nAryTree(8)
tree.insert(2)
tree.insert(3)
tree.insert(29)
print(nAry_Levelorder(tree))

tree = nAryTree(2)
tree.insert(1)
tree.insert(6)
tree.insert(9)
print(nAry_Levelorder(tree))
