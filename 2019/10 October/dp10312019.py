#  This problem was recently asked by Uber:

# Given a linked list, determine if the linked list has a cycle in it.
# For notation purposes, we use an integer pos which represents the zero-indexed position where the tail connects to.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        # Fill this in.
        s = set()
        temp = head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next

        return False


testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail
testTail.next = node1

print(Solution().hasCycle(testHead))
# True
