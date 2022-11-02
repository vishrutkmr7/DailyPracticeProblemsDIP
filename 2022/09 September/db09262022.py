"""
Given two linked lists that represent two numbers, return the sum of the numbers also represented as a list.

Ex: Given the two linked lists…

a = 1->2, b = 1->3, return a list that looks as follows: 2->5
Ex: Given the two linked lists…

a = 1->9, b = 1, return a list that looks as follows: 2->0
"""

# Definition for singly-linked list.
class ListNode:
    def arrayToList(self, array):
        if not array:
            return None
        head = ListNode(array[0])
        current = head
        for i in range(1, len(array)):
            current.next = ListNode(array[i])
            current = current.next
        return head

    def listToArray(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s = 0
        l = ListNode()
        n = l
        s1 = ""
        s2 = ""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        s = int(s1[::-1]) + int(s2[::-1])
        t = 1
        for i in str(s)[::-1]:
            n.val = int(i)
            if t == len(str(s)):
                break
            t += 1
            n.next = ListNode()
            n = n.next
        return l


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode().arrayToList([1, 2])
    l2 = ListNode().arrayToList([1, 3])
    print(solution.addTwoNumbers(l1, l2))
    l1 = ListNode().arrayToList([1, 9])
    l2 = ListNode().arrayToList([1])
    print(solution.addTwoNumbers(l1, l2))
