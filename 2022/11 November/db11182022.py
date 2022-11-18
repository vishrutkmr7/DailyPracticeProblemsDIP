"""
Given a reference to a linked list, return whether or not it forms a palindrome. 

Ex: Given a reference to the following linked list...

head = 1->3->1, return true.
Ex: Given a reference to the following linked list...

head = 1->7, return false.
"""

from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string = ""
        while head:
            string += str(head.val)
            head = head.next
        return string == string[::-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(1)
    print(solution.isPalindrome(head))

    head = ListNode(1)
    head.next = ListNode(7)
    print(solution.isPalindrome(head))
