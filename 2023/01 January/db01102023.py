"""
Given a positive integer, num, return whether or not it forms a palindrome.
Note: You may not transform the number into a string.

Ex: Given the following num…

num = 12321, return true.
Ex: Given the following num…

num = 5393, return false.
"""


class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        original = num
        reverse = 0
        while num > 0:
            reverse = reverse * 10 + num % 10
            num //= 10
        return original == reverse


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome(12321) == True
    assert solution.isPalindrome(5393) == False
    print("All tests passed.")
