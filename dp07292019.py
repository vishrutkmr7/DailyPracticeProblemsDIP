# Definition for singly-linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    p1 = l1
    p2 = l2
    i = 0
    j = 0
    n1 = 0
    n2 = 0
    while p1:
        n1 += p1.val * (10 ** i)
        i +=1
        p1 = p1.next

    while p2:
        n2 += p2.val * (10 ** j)
        j +=1
        p2 = p2.next

    sum = n1 + n2

    if len(str(sum)) == 4:
        l3 = ListNode(str(sum)[3])
        l3.next = ListNode(str(sum)[2])
        l3.next.next = ListNode(str(sum)[1])
        l3.next.next.next = ListNode(str(sum)[0])
    elif len(str(sum)) == 3:
        l3 = ListNode(str(sum)[2])
        l3.next = ListNode(str(sum)[1])
        l3.next.next = ListNode(str(sum)[0])
    
    # print("n1", n1, "n2", n2)
    return l3

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val),
  result = result.next
# 7 0 8