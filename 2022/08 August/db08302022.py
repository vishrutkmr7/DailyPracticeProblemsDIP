"""
This question is asked by Facebook.
Given two integers x and y, return the hamming distance between the two numbers.
Note: The hamming distance between two numbers is the number of bit positions in which the bits differ.

Ex: Given the following integers x and y…

x = 2, y = 4, return 2.
2 in binary is 0 0 1 0
4 in binary is 0 1 0 0
therefore the number of positions in which the bits differ is two.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingDistance(2, 4))
