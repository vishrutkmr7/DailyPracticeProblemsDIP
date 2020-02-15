# Definition for singly-linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in.
        p1 = l1
        p2 = l2
        i = 0
        j = 0
        n1 = 0
        n2 = 0
        while p1:
            n1 += p1.val * (10 ** i)
            i += 1
            p1 = p1.next

        while p2:
            n2 += p2.val * (10 ** j)
            j += 1
            p2 = p2.next

        s = n1 + n2

        start_node = node = ListNode(str(s)[-1])  # initialize to last character in s
        for c in reversed(str(s)[:-1]):
            node.next = ListNode(c)
            node = node.next

        # print("n1", n1, "n2", n2)
        return start_node


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val),
    result = result.next
# 7 0 8
